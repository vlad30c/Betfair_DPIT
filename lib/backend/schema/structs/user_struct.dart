// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class UserStruct extends BaseStruct {
  UserStruct({
    String? token,
    String? userId,
    String? email,
    String? displayName,
    String? profilePicture,
    String? authProvider,
    String? phoneNumber,
    String? username,
  })  : _token = token,
        _userId = userId,
        _email = email,
        _displayName = displayName,
        _profilePicture = profilePicture,
        _authProvider = authProvider,
        _phoneNumber = phoneNumber,
        _username = username;

  // "token" field.
  String? _token;
  String get token => _token ?? '';
  set token(String? val) => _token = val;

  bool hasToken() => _token != null;

  // "user_id" field.
  String? _userId;
  String get userId => _userId ?? '';
  set userId(String? val) => _userId = val;

  bool hasUserId() => _userId != null;

  // "email" field.
  String? _email;
  String get email => _email ?? '';
  set email(String? val) => _email = val;

  bool hasEmail() => _email != null;

  // "display_name" field.
  String? _displayName;
  String get displayName => _displayName ?? '';
  set displayName(String? val) => _displayName = val;

  bool hasDisplayName() => _displayName != null;

  // "profile_picture" field.
  String? _profilePicture;
  String get profilePicture => _profilePicture ?? '';
  set profilePicture(String? val) => _profilePicture = val;

  bool hasProfilePicture() => _profilePicture != null;

  // "auth_provider" field.
  String? _authProvider;
  String get authProvider => _authProvider ?? '';
  set authProvider(String? val) => _authProvider = val;

  bool hasAuthProvider() => _authProvider != null;

  // "phone_number" field.
  String? _phoneNumber;
  String get phoneNumber => _phoneNumber ?? '';
  set phoneNumber(String? val) => _phoneNumber = val;

  bool hasPhoneNumber() => _phoneNumber != null;

  // "username" field.
  String? _username;
  String get username => _username ?? '';
  set username(String? val) => _username = val;

  bool hasUsername() => _username != null;

  static UserStruct fromMap(Map<String, dynamic> data) => UserStruct(
        token: data['token'] as String?,
        userId: data['user_id'] as String?,
        email: data['email'] as String?,
        displayName: data['display_name'] as String?,
        profilePicture: data['profile_picture'] as String?,
        authProvider: data['auth_provider'] as String?,
        phoneNumber: data['phone_number'] as String?,
        username: data['username'] as String?,
      );

  static UserStruct? maybeFromMap(dynamic data) =>
      data is Map ? UserStruct.fromMap(data.cast<String, dynamic>()) : null;

  Map<String, dynamic> toMap() => {
        'token': _token,
        'user_id': _userId,
        'email': _email,
        'display_name': _displayName,
        'profile_picture': _profilePicture,
        'auth_provider': _authProvider,
        'phone_number': _phoneNumber,
        'username': _username,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'token': serializeParam(
          _token,
          ParamType.String,
        ),
        'user_id': serializeParam(
          _userId,
          ParamType.String,
        ),
        'email': serializeParam(
          _email,
          ParamType.String,
        ),
        'display_name': serializeParam(
          _displayName,
          ParamType.String,
        ),
        'profile_picture': serializeParam(
          _profilePicture,
          ParamType.String,
        ),
        'auth_provider': serializeParam(
          _authProvider,
          ParamType.String,
        ),
        'phone_number': serializeParam(
          _phoneNumber,
          ParamType.String,
        ),
        'username': serializeParam(
          _username,
          ParamType.String,
        ),
      }.withoutNulls;

  static UserStruct fromSerializableMap(Map<String, dynamic> data) =>
      UserStruct(
        token: deserializeParam(
          data['token'],
          ParamType.String,
          false,
        ),
        userId: deserializeParam(
          data['user_id'],
          ParamType.String,
          false,
        ),
        email: deserializeParam(
          data['email'],
          ParamType.String,
          false,
        ),
        displayName: deserializeParam(
          data['display_name'],
          ParamType.String,
          false,
        ),
        profilePicture: deserializeParam(
          data['profile_picture'],
          ParamType.String,
          false,
        ),
        authProvider: deserializeParam(
          data['auth_provider'],
          ParamType.String,
          false,
        ),
        phoneNumber: deserializeParam(
          data['phone_number'],
          ParamType.String,
          false,
        ),
        username: deserializeParam(
          data['username'],
          ParamType.String,
          false,
        ),
      );

  @override
  String toString() => 'UserStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    return other is UserStruct &&
        token == other.token &&
        userId == other.userId &&
        email == other.email &&
        displayName == other.displayName &&
        profilePicture == other.profilePicture &&
        authProvider == other.authProvider &&
        phoneNumber == other.phoneNumber &&
        username == other.username;
  }

  @override
  int get hashCode => const ListEquality().hash([
        token,
        userId,
        email,
        displayName,
        profilePicture,
        authProvider,
        phoneNumber,
        username
      ]);
}

UserStruct createUserStruct({
  String? token,
  String? userId,
  String? email,
  String? displayName,
  String? profilePicture,
  String? authProvider,
  String? phoneNumber,
  String? username,
}) =>
    UserStruct(
      token: token,
      userId: userId,
      email: email,
      displayName: displayName,
      profilePicture: profilePicture,
      authProvider: authProvider,
      phoneNumber: phoneNumber,
      username: username,
    );
