import 'dart:convert';
import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:intl/intl.dart';
import 'package:timeago/timeago.dart' as timeago;
import 'lat_lng.dart';
import 'place.dart';
import 'uploaded_file.dart';
import '/backend/schema/structs/index.dart';
import '/auth/custom_auth/auth_util.dart';

/// turns the cuisine and setting lists into a single string, with its values
/// separated by commas so it can be passed as a get query parameter
String? tagListToCommaString(
  List<String>? cuisineList,
  List<String>? settingList,
) {
  final combined = [
    if (cuisineList != null) ...cuisineList,
    if (settingList != null) ...settingList,
  ];

  if (combined.isEmpty) return '';
  return combined.map((e) => e.toString()).join(',');
}

String? priceListToCommaString(List<String>? priceList) {
  if (priceList == null || priceList.isEmpty) return '';
  return priceList.map((e) => e.toString()).join(',');
}
