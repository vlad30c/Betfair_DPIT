import 'dart:convert';

import 'package:flutter/foundation.dart';

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

    return ApiManager.instance.makeApiCall(
      callName: 'Create Account',
      apiUrl: '${baseUrl}/registration',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
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
  "${escapeStringForJson(password)}": "123456"
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'Log in',
      apiUrl: '${baseUrl}/login',
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

class ForgotPasswordCall {
  Future<ApiCallResponse> call({
    String? username = '',
    String? email = '',
  }) async {
    final baseUrl = AuthenticationGroup.getBaseUrl(
      username: username,
      email: email,
    );

    return ApiManager.instance.makeApiCall(
      callName: 'Forgot Password',
      apiUrl: '${baseUrl}/password',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
      },
      params: {},
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

/// End authentication Group Code

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
