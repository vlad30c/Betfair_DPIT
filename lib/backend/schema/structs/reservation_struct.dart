// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class ReservationStruct extends BaseStruct {
  ReservationStruct({
    String? fullName,
  }) : _fullName = fullName;

  // "FullName" field.
  String? _fullName;
  String get fullName => _fullName ?? '';
  set fullName(String? val) => _fullName = val;

  bool hasFullName() => _fullName != null;

  static ReservationStruct fromMap(Map<String, dynamic> data) =>
      ReservationStruct(
        fullName: data['FullName'] as String?,
      );

  static ReservationStruct? maybeFromMap(dynamic data) => data is Map
      ? ReservationStruct.fromMap(data.cast<String, dynamic>())
      : null;

  Map<String, dynamic> toMap() => {
        'FullName': _fullName,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'FullName': serializeParam(
          _fullName,
          ParamType.String,
        ),
      }.withoutNulls;

  static ReservationStruct fromSerializableMap(Map<String, dynamic> data) =>
      ReservationStruct(
        fullName: deserializeParam(
          data['FullName'],
          ParamType.String,
          false,
        ),
      );

  @override
  String toString() => 'ReservationStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    return other is ReservationStruct && fullName == other.fullName;
  }

  @override
  int get hashCode => const ListEquality().hash([fullName]);
}

ReservationStruct createReservationStruct({
  String? fullName,
}) =>
    ReservationStruct(
      fullName: fullName,
    );
