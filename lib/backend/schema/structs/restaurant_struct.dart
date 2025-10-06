// ignore_for_file: unnecessary_getters_setters

import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class RestaurantStruct extends BaseStruct {
  RestaurantStruct({
    String? name,
    String? description,
    String? priceLevel,
    bool? isFavorite,
  })  : _name = name,
        _description = description,
        _priceLevel = priceLevel,
        _isFavorite = isFavorite;

  // "name" field.
  String? _name;
  String get name => _name ?? '';
  set name(String? val) => _name = val;

  bool hasName() => _name != null;

  // "description" field.
  String? _description;
  String get description => _description ?? '';
  set description(String? val) => _description = val;

  bool hasDescription() => _description != null;

  // "price_level" field.
  String? _priceLevel;
  String get priceLevel => _priceLevel ?? '';
  set priceLevel(String? val) => _priceLevel = val;

  bool hasPriceLevel() => _priceLevel != null;

  // "isFavorite" field.
  bool? _isFavorite;
  bool get isFavorite => _isFavorite ?? false;
  set isFavorite(bool? val) => _isFavorite = val;

  bool hasIsFavorite() => _isFavorite != null;

  static RestaurantStruct fromMap(Map<String, dynamic> data) =>
      RestaurantStruct(
        name: data['name'] as String?,
        description: data['description'] as String?,
        priceLevel: data['price_level'] as String?,
        isFavorite: data['isFavorite'] as bool?,
      );

  static RestaurantStruct? maybeFromMap(dynamic data) => data is Map
      ? RestaurantStruct.fromMap(data.cast<String, dynamic>())
      : null;

  Map<String, dynamic> toMap() => {
        'name': _name,
        'description': _description,
        'price_level': _priceLevel,
        'isFavorite': _isFavorite,
      }.withoutNulls;

  @override
  Map<String, dynamic> toSerializableMap() => {
        'name': serializeParam(
          _name,
          ParamType.String,
        ),
        'description': serializeParam(
          _description,
          ParamType.String,
        ),
        'price_level': serializeParam(
          _priceLevel,
          ParamType.String,
        ),
        'isFavorite': serializeParam(
          _isFavorite,
          ParamType.bool,
        ),
      }.withoutNulls;

  static RestaurantStruct fromSerializableMap(Map<String, dynamic> data) =>
      RestaurantStruct(
        name: deserializeParam(
          data['name'],
          ParamType.String,
          false,
        ),
        description: deserializeParam(
          data['description'],
          ParamType.String,
          false,
        ),
        priceLevel: deserializeParam(
          data['price_level'],
          ParamType.String,
          false,
        ),
        isFavorite: deserializeParam(
          data['isFavorite'],
          ParamType.bool,
          false,
        ),
      );

  @override
  String toString() => 'RestaurantStruct(${toMap()})';

  @override
  bool operator ==(Object other) {
    return other is RestaurantStruct &&
        name == other.name &&
        description == other.description &&
        priceLevel == other.priceLevel &&
        isFavorite == other.isFavorite;
  }

  @override
  int get hashCode =>
      const ListEquality().hash([name, description, priceLevel, isFavorite]);
}

RestaurantStruct createRestaurantStruct({
  String? name,
  String? description,
  String? priceLevel,
  bool? isFavorite,
}) =>
    RestaurantStruct(
      name: name,
      description: description,
      priceLevel: priceLevel,
      isFavorite: isFavorite,
    );
