import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {
    prefs = await SharedPreferences.getInstance();
    _safeInit(() {
      _token = prefs.getString('ff_token') ?? _token;
    });
    _safeInit(() {
      _selectedCity = prefs.getString('ff_selectedCity') ?? _selectedCity;
    });
  }

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  late SharedPreferences prefs;

  DateTime? _selectedDate;
  DateTime? get selectedDate => _selectedDate;
  set selectedDate(DateTime? value) {
    _selectedDate = value;
  }

  String _token = '';
  String get token => _token;
  set token(String value) {
    _token = value;
    prefs.setString('ff_token', value);
  }

  String _selectedCity = 'Cluj-Napoca';
  String get selectedCity => _selectedCity;
  set selectedCity(String value) {
    _selectedCity = value;
    prefs.setString('ff_selectedCity', value);
  }

  List<String> _selectedCuisines = [];
  List<String> get selectedCuisines => _selectedCuisines;
  set selectedCuisines(List<String> value) {
    _selectedCuisines = value;
  }

  void addToSelectedCuisines(String value) {
    selectedCuisines.add(value);
  }

  void removeFromSelectedCuisines(String value) {
    selectedCuisines.remove(value);
  }

  void removeAtIndexFromSelectedCuisines(int index) {
    selectedCuisines.removeAt(index);
  }

  void updateSelectedCuisinesAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    selectedCuisines[index] = updateFn(_selectedCuisines[index]);
  }

  void insertAtIndexInSelectedCuisines(int index, String value) {
    selectedCuisines.insert(index, value);
  }

  List<String> _selectedSettings = [];
  List<String> get selectedSettings => _selectedSettings;
  set selectedSettings(List<String> value) {
    _selectedSettings = value;
  }

  void addToSelectedSettings(String value) {
    selectedSettings.add(value);
  }

  void removeFromSelectedSettings(String value) {
    selectedSettings.remove(value);
  }

  void removeAtIndexFromSelectedSettings(int index) {
    selectedSettings.removeAt(index);
  }

  void updateSelectedSettingsAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    selectedSettings[index] = updateFn(_selectedSettings[index]);
  }

  void insertAtIndexInSelectedSettings(int index, String value) {
    selectedSettings.insert(index, value);
  }

  List<String> _selectedPriceLevel = [];
  List<String> get selectedPriceLevel => _selectedPriceLevel;
  set selectedPriceLevel(List<String> value) {
    _selectedPriceLevel = value;
  }

  void addToSelectedPriceLevel(String value) {
    selectedPriceLevel.add(value);
  }

  void removeFromSelectedPriceLevel(String value) {
    selectedPriceLevel.remove(value);
  }

  void removeAtIndexFromSelectedPriceLevel(int index) {
    selectedPriceLevel.removeAt(index);
  }

  void updateSelectedPriceLevelAtIndex(
    int index,
    String Function(String) updateFn,
  ) {
    selectedPriceLevel[index] = updateFn(_selectedPriceLevel[index]);
  }

  void insertAtIndexInSelectedPriceLevel(int index, String value) {
    selectedPriceLevel.insert(index, value);
  }

  String _reservationHour = '';
  String get reservationHour => _reservationHour;
  set reservationHour(String value) {
    _reservationHour = value;
  }
}

void _safeInit(Function() initializeField) {
  try {
    initializeField();
  } catch (_) {}
}

Future _safeInitAsync(Function() initializeField) async {
  try {
    await initializeField();
  } catch (_) {}
}
