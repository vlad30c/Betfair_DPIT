import 'dart:convert';

import 'package:flutter/foundation.dart';

import '/flutter_flow/flutter_flow_util.dart';
import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

/// Start authentication Group Code

class AuthenticationGroup {
  static String getBaseUrl({
    String? username = '',
    String? email = '',
  }) =>
      'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/api/auth/';
  static Map<String, String> headers = {
    'Content-Type': 'application/json',
  };
  static CreateAccountCall createAccountCall = CreateAccountCall();
  static LogInCall logInCall = LogInCall();
  static ForgotPasswordCall forgotPasswordCall = ForgotPasswordCall();
  static LogOutCall logOutCall = LogOutCall();
}

class CreateAccountCall {
  Future<ApiCallResponse> call({
    String? password1 = '',
    String? password2 = '',
    String? username = '',
    String? email = '',
  }) async {
    final baseUrl = AuthenticationGroup.getBaseUrl(
      username: username,
      email: email,
    );

    final ffApiRequestBody = '''
{
  "username": "${escapeStringForJson(username)}",
  "email": "${escapeStringForJson(email)}",
  "password1": "${escapeStringForJson(password1)}",
  "password2": "${escapeStringForJson(password2)}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Create Account',
      apiUrl: '${baseUrl}registration/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  String? key(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.key''',
      ));
}

class LogInCall {
  Future<ApiCallResponse> call({
    String? password = '',
    String? username = '',
    String? email = '',
  }) async {
    final baseUrl = AuthenticationGroup.getBaseUrl(
      username: username,
      email: email,
    );

    final ffApiRequestBody = '''
{
  "username": "${escapeStringForJson(username)}",
  "email": "${escapeStringForJson(email)}",
  "password": "${escapeStringForJson(password)}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Log in',
      apiUrl: '${baseUrl}login/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  String? key(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.key''',
      ));
}

class ForgotPasswordCall {
  Future<ApiCallResponse> call({
    String? username = '',
    String? email = '',
  }) async {
    final baseUrl = AuthenticationGroup.getBaseUrl(
      username: username,
      email: email,
    );

    final ffApiRequestBody = '''
{
  "username": "${escapeStringForJson(username)}",
  "email": "${escapeStringForJson(email)}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Forgot Password',
      apiUrl: '${baseUrl}password/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

class LogOutCall {
  Future<ApiCallResponse> call({
    String? username = '',
    String? email = '',
  }) async {
    final baseUrl = AuthenticationGroup.getBaseUrl(
      username: username,
      email: email,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'Log out',
      apiUrl: '${baseUrl}/logout/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
      bodyType: BodyType.NONE,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

/// End authentication Group Code

/// Start restaurant Group Code

class RestaurantGroup {
  static String getBaseUrl({
    String? authToken = '',
  }) =>
      'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/';
  static Map<String, String> headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token [auth_token]',
  };
  static GetFilteredRestaurantListCall getFilteredRestaurantListCall =
      GetFilteredRestaurantListCall();
  static GetUniqueCitiesCall getUniqueCitiesCall = GetUniqueCitiesCall();
}

class GetFilteredRestaurantListCall {
  Future<ApiCallResponse> call({
    String? tags = '',
    String? search = '',
    String? city = '',
    String? priceLevel = '',
    String? authToken = '',
  }) async {
    final baseUrl = RestaurantGroup.getBaseUrl(
      authToken: authToken,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'getFilteredRestaurantList',
      apiUrl: '${baseUrl}restaurants/',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {
        'tags': tags,
        'search': search,
        'city': city,
        'price_level': priceLevel,
      },
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  List<String>? restaurantName(dynamic response) => (getJsonField(
        response,
        r'''$.restaurants[:].name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<String>? restaurantPhoto(dynamic response) => (getJsonField(
        response,
        r'''$.restaurants[:].first_photo''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<bool>? isFavorite(dynamic response) => (getJsonField(
        response,
        r'''$.restaurants[:].is_favorited''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<bool>(x))
          .withoutNulls
          .toList();
  List<int>? restaurantId(dynamic response) => (getJsonField(
        response,
        r'''$.restaurants[:].restaurant_id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
}

class GetUniqueCitiesCall {
  Future<ApiCallResponse> call({
    String? search = '',
    String? authToken = '',
  }) async {
    final baseUrl = RestaurantGroup.getBaseUrl(
      authToken: authToken,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'getUniqueCities',
      apiUrl: '${baseUrl}/restaurants/cities/',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {
        'search': search,
      },
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

/// End restaurant Group Code

/// Start favorites Group Code

class FavoritesGroup {
  static String getBaseUrl({
    String? authToken = '',
  }) =>
      'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/';
  static Map<String, String> headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token [auth_token]',
  };
  static ToggleFavoriteCall toggleFavoriteCall = ToggleFavoriteCall();
  static FavoritesListCall favoritesListCall = FavoritesListCall();
}

class ToggleFavoriteCall {
  Future<ApiCallResponse> call({
    int? restaurant,
    String? authToken = '',
  }) async {
    final baseUrl = FavoritesGroup.getBaseUrl(
      authToken: authToken,
    );

    final ffApiRequestBody = '''
{
  "restaurant": ${restaurant}
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Toggle Favorite',
      apiUrl: '${baseUrl}/favorites/toggle/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  String? message(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.message''',
      ));
  bool? favoritedStatus(dynamic response) => castToType<bool>(getJsonField(
        response,
        r'''$.favorited''',
      ));
}

class FavoritesListCall {
  Future<ApiCallResponse> call({
    String? authToken = '',
  }) async {
    final baseUrl = FavoritesGroup.getBaseUrl(
      authToken: authToken,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'Favorites List',
      apiUrl: '${baseUrl}favorites/',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  List<String>? restaurantName(dynamic response) => (getJsonField(
        response,
        r'''$.favorites[:].restaurant.name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<String>? restaurantPrice(dynamic response) => (getJsonField(
        response,
        r'''$.favorites[:].restaurant.price_level''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<String>? restaurantFirstPhoto(dynamic response) => (getJsonField(
        response,
        r'''$.favorites[:].restaurant.first_photo''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<int>? restaurantID(dynamic response) => (getJsonField(
        response,
        r'''$.favorites[:].restaurant.restaurant_id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
}

/// End favorites Group Code

/// Start bookings Group Code

class BookingsGroup {
  static String getBaseUrl({
    String? authToken = '',
  }) =>
      'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/';
  static Map<String, String> headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Token [auth_token]',
  };
  static GetBookingsListCall getBookingsListCall = GetBookingsListCall();
  static CreateNewBookingCall createNewBookingCall = CreateNewBookingCall();
}

class GetBookingsListCall {
  Future<ApiCallResponse> call({
    String? authToken = '',
  }) async {
    final baseUrl = BookingsGroup.getBaseUrl(
      authToken: authToken,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'Get Bookings List',
      apiUrl: '${baseUrl}reservations/',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  List<int>? restaurantID(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].restaurant''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
  List<int>? guests(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].number_of_guests''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
  List<String>? date(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].reservation_date''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<String>? time(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].reservation_time''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<String>? phoneNumber(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].phone_number''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
  List<int>? reservationID(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].reservation_id''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<int>(x))
          .withoutNulls
          .toList();
  List<String>? fullName(dynamic response) => (getJsonField(
        response,
        r'''$.reservations[:].full_name''',
        true,
      ) as List?)
          ?.withoutNulls
          .map((x) => castToType<String>(x))
          .withoutNulls
          .toList();
}

class CreateNewBookingCall {
  Future<ApiCallResponse> call({
    int? restaurantID,
    String? reservationDate = '',
    String? reservationTime = '',
    int? noGuests,
    String? specialRequests = '',
    String? phoneNumber = '',
    String? fullName = '',
    String? authToken = '',
  }) async {
    final baseUrl = BookingsGroup.getBaseUrl(
      authToken: authToken,
    );

    final ffApiRequestBody = '''
{
  "restaurant": ${restaurantID},
  "reservation_date": "${escapeStringForJson(reservationDate)}",
  "reservation_time": "${escapeStringForJson(reservationTime)}",
  "number_of_guests": ${noGuests},
  "special_requests": "${escapeStringForJson(specialRequests)}",
  "phone_number": "${escapeStringForJson(phoneNumber)}",
  "full_name": "${escapeStringForJson(fullName)}"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Create new Booking',
      apiUrl: '${baseUrl}reservations/',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      body: ffApiRequestBody,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }

  bool? success(dynamic response) => castToType<bool>(getJsonField(
        response,
        r'''$.success''',
      ));
  String? message(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.message''',
      ));
  int? reservationID(dynamic response) => castToType<int>(getJsonField(
        response,
        r'''$.reservation.reservation_id''',
      ));
  int? restaurantID(dynamic response) => castToType<int>(getJsonField(
        response,
        r'''$.reservation.restaurant''',
      ));
  String? date(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.reservation.reservation_date''',
      ));
  String? time(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.reservation.reservation_time''',
      ));
  int? noGuests(dynamic response) => castToType<int>(getJsonField(
        response,
        r'''$.reservation.number_of_guests''',
      ));
  String? requests(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.reservation.special_requests''',
      ));
  String? phoneNumber(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.reservation.phone_number''',
      ));
  String? fullName(dynamic response) => castToType<String>(getJsonField(
        response,
        r'''$.reservation.full_name''',
      ));
}

/// End bookings Group Code

class UpdateUserDataCall {
  static Future<ApiCallResponse> call({
    String? firstName = '',
    String? lastName = '',
    String? email = '',
    dynamic profileJson,
    String? phoneNumber = '',
    String? profilePicture = '',
    String? authToken = '',
  }) async {
    final profile = _serializeJson(profileJson);

    return ApiManager.instance.makeApiCall(
      callName: 'Update User Data',
      apiUrl:
          'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/api/me/update/',
      callType: ApiCallType.PATCH,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      bodyType: BodyType.NONE,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

class GetCurrentUserDataCall {
  static Future<ApiCallResponse> call({
    String? authToken = '',
  }) async {
    return ApiManager.instance.makeApiCall(
      callName: 'Get Current User Data',
      apiUrl:
          'http://bite-app-d4fnhqf3hzd7cngg.northeurope-01.azurewebsites.net/api/users/me/',
      callType: ApiCallType.GET,
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ${authToken}',
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
      isStreamingApi: false,
      alwaysAllowBody: false,
    );
  }
}

class ApiPagingParams {
  int nextPageNumber = 0;
  int numItems = 0;
  dynamic lastResponse;

  ApiPagingParams({
    required this.nextPageNumber,
    required this.numItems,
    required this.lastResponse,
  });

  @override
  String toString() =>
      'PagingParams(nextPageNumber: $nextPageNumber, numItems: $numItems, lastResponse: $lastResponse,)';
}

String _toEncodable(dynamic item) {
  return item;
}

String _serializeList(List? list) {
  list ??= <String>[];
  try {
    return json.encode(list, toEncodable: _toEncodable);
  } catch (_) {
    if (kDebugMode) {
      print("List serialization failed. Returning empty list.");
    }
    return '[]';
  }
}

String _serializeJson(dynamic jsonVar, [bool isList = false]) {
  jsonVar ??= (isList ? [] : {});
  try {
    return json.encode(jsonVar, toEncodable: _toEncodable);
  } catch (_) {
    if (kDebugMode) {
      print("Json serialization failed. Returning empty json.");
    }
    return isList ? '[]' : '{}';
  }
}

String? escapeStringForJson(String? input) {
  if (input == null) {
    return null;
  }
  return input
      .replaceAll('\\', '\\\\')
      .replaceAll('"', '\\"')
      .replaceAll('\n', '\\n')
      .replaceAll('\t', '\\t');
}
