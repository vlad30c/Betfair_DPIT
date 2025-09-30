// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class RestaurantStruct extends BaseStruct {
  RestaurantStruct({
    String? name,
  }) : _name = name;

  // "name" field.
  String? _name;
  String get name => _name ?? '';
  set name(String? val) => _name = val;

  bool hasName() => _name != null;

  static RestaurantStruct fromMap(Map<String, dynamic> data) =>
      RestaurantStruct(
        name: data['name'] as String?,
      );

  static RestaurantStruct? maybeFromMap(dynamic data) => data is Map
      ? RestaurantStruct.fromMap(data.cast<String, dynamic>())
      : null;

  Map<String, dynamic> toMap() => {
        'name': _name,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'name': serializeParam(
          _name,
          ParamType.String,
        ),
      }.withoutNulls;

  static RestaurantStruct fromSerializableMap(Map<String, dynamic> data) =>
      RestaurantStruct(
        name: deserializeParam(
          data['name'],
          ParamType.String,
          false,
        ),
      );

  @override
  String toString() => 'RestaurantStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    return other is RestaurantStruct && name == other.name;
  }

  @override
  int get hashCode => const ListEquality().hash([name]);
}

RestaurantStruct createRestaurantStruct({
  String? name,
}) =>
    RestaurantStruct(
      name: name,
    );
