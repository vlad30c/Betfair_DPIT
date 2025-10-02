import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bite_backend.settings")  # replace with your project name
django.setup()

import gspread
import pandas as pd
from google.oauth2.service_account import Credentials
from django.utils.dateparse import parse_time
from bite.models import Restaurants, RestaurantSchedules, Tags, RestaurantFiles  # adjust app name
import datetime


# === SETUP ===
PROCESSED_SPREADSHEET_ID = "1YuDCMWYbsqxcHMZhS530tAQrUSqRsPNu5wxxQwH5H4w"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(
    "bite/credentials/service_account.json", scopes=SCOPES
)
gc = gspread.authorize(creds)

# === OPEN SHEET ===
processed_sh = gc.open_by_key(PROCESSED_SPREADSHEET_ID)

restaurants_ws = processed_sh.worksheet("Restaurants")
schedules_ws = processed_sh.worksheet("RestaurantSchedules")
tags_ws = processed_sh.worksheet("RestaurantTags")
files_ws = processed_sh.worksheet("RestaurantFiles")

# --- READ DATA INTO DATAFRAMES (preserve raw values like +40, 07...) ---
rows = restaurants_ws.get_all_values()
restaurants_df = pd.DataFrame(rows[1:], columns=rows[0])

rows = schedules_ws.get_all_values()
schedules_df = pd.DataFrame(rows[1:], columns=rows[0])

rows = tags_ws.get_all_values()
tags_df = pd.DataFrame(rows[1:], columns=rows[0])

rows = files_ws.get_all_values()
files_df = pd.DataFrame(rows[1:], columns=rows[0])

# --- IMPORT RESTAURANTS AND RELATED DATA ---
for _, row in restaurants_df.iterrows():
    email = row["Email"].strip() if row["Email"] else None

    # Check if restaurant exists by email
    restaurant, created = Restaurants.objects.get_or_create(
        email=email,
        defaults={
            "name": str(row.get("Restaurant Name") or "").strip(),
            "description": str(row.get("Description") or "").strip() or None,
            "phone_number": str(row.get("Phone") or "").strip() or None,
            "website": str(row.get("Website") or "").strip() or None,
            "address": str(row.get("Address") or "").strip(),
            "city": str(row.get("City") or "").strip() or None,
            "latitude": float(row.get("Latitude") or 0.0),
            "longitude": float(row.get("Longitude") or 0.0),
            "price_level": str(row.get("Price Level") or "average").strip(),
        }
    )

    external_id = row["Restaurant External ID"]  # internal lookup

    # --- IMPORT TAGS ---
    restaurant_tags = tags_df[tags_df["Restaurant External ID"] == external_id]
    for _, tag_row in restaurant_tags.iterrows():
        tag_name = tag_row["Tag"].strip().title()
        category = tag_row["Category"].strip().lower()
        tag_obj, _ = Tags.objects.get_or_create(name=tag_name, defaults={"category": category})
        restaurant.tags.add(tag_obj) # Many-to-many auto-avoids duplicates

    # --- IMPORT SCHEDULES ---
    restaurant_schedules = schedules_df[schedules_df["Restaurant External ID"] == external_id]
    for _, sched_row in restaurant_schedules.iterrows():
        open_time = parse_time(sched_row["Open Time"])
        close_time = parse_time(sched_row["Close Time"])
        # Check if schedule already exists
        schedule, _ = RestaurantSchedules.objects.get_or_create(
            restaurant=restaurant,
            day_of_week=sched_row["Day"].strip(),
            open_time=open_time,
            close_time=close_time
        )

    # --- IMPORT FILES ---
    restaurant_files = files_df[files_df["Restaurant External ID"] == external_id]
    for _, file_row in restaurant_files.iterrows():
        uploaded_at = None
        if file_row.get("Uploaded At UTC"):
            try:
                uploaded_at = datetime.datetime.fromisoformat(file_row["Uploaded At UTC"])
            except ValueError:
                uploaded_at = None

         # Check if file already exists
        file_obj, _ = RestaurantFiles.objects.get_or_create(
            restaurant=restaurant,
            file_url=file_row["File URL"].strip(),
            defaults={
                "type": file_row["Type"].strip(),
                "uploaded_at_utc": uploaded_at
            }
        )

print("✅ Import complete!")
