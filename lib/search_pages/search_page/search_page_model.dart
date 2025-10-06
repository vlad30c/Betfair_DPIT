import '/flutter_flow/flutter_flow_util.dart';
import '/index.dart';
import 'search_page_widget.dart' show SearchPageWidget;
import 'package:flutter/material.dart';

class SearchPageModel extends FlutterFlowModel<SearchPageWidget> {
  ///  Local state fields for this page.

  String? selectedSetting;

  List<bool> favoriteStatus = [];
  void addToFavoriteStatus(bool item) => favoriteStatus.add(item);
  void removeFromFavoriteStatus(bool item) => favoriteStatus.remove(item);
  void removeAtIndexFromFavoriteStatus(int index) =>
      favoriteStatus.removeAt(index);
  void insertAtIndexInFavoriteStatus(int index, bool item) =>
      favoriteStatus.insert(index, item);
  void updateFavoriteStatusAtIndex(int index, Function(bool) updateFn) =>
      favoriteStatus[index] = updateFn(favoriteStatus[index]);

  ///  State fields for stateful widgets in this page.

  // State field(s) for TextField widget.
  FocusNode? textFieldFocusNode;
  TextEditingController? textController;
  String? Function(BuildContext, String?)? textControllerValidator;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    textFieldFocusNode?.dispose();
    textController?.dispose();
  }
}
