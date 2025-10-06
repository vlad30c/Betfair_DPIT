import '/flutter_flow/flutter_flow_util.dart';
import '/index.dart';
import 'booking_new_widget.dart' show BookingNewWidget;
import 'package:flutter/material.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';

class BookingNewModel extends FlutterFlowModel<BookingNewWidget> {
  ///  Local state fields for this page.

  DateTime? reservationHour;

  ///  State fields for stateful widgets in this page.

  final formKey = GlobalKey<FormState>();
  // State field(s) for fullName widget.
  FocusNode? fullNameFocusNode;
  TextEditingController? fullNameTextController;
  String? Function(BuildContext, String?)? fullNameTextControllerValidator;
  String? _fullNameTextControllerValidator(BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the full name for the reservation';
    }

    return null;
  }

  // State field(s) for phoneNumber widget.
  FocusNode? phoneNumberFocusNode;
  TextEditingController? phoneNumberTextController;
  String? Function(BuildContext, String?)? phoneNumberTextControllerValidator;
  String? _phoneNumberTextControllerValidator(
      BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter a valid phone number.';
    }

    return null;
  }

  // State field(s) for NumberOfGuests widget.
  FocusNode? numberOfGuestsFocusNode;
  TextEditingController? numberOfGuestsTextController;
  late MaskTextInputFormatter numberOfGuestsMask;
  String? Function(BuildContext, String?)?
      numberOfGuestsTextControllerValidator;
  String? _numberOfGuestsTextControllerValidator(
      BuildContext context, String? val) {
    if (val == null || val.isEmpty) {
      return 'Please enter the number of guests the reservation is for.';
    }

    return null;
  }

  // State field(s) for message widget.
  FocusNode? messageFocusNode;
  TextEditingController? messageTextController;
  String? Function(BuildContext, String?)? messageTextControllerValidator;

  @override
  void initState(BuildContext context) {
    fullNameTextControllerValidator = _fullNameTextControllerValidator;
    phoneNumberTextControllerValidator = _phoneNumberTextControllerValidator;
    numberOfGuestsTextControllerValidator =
        _numberOfGuestsTextControllerValidator;
  }

  @override
  void dispose() {
    fullNameFocusNode?.dispose();
    fullNameTextController?.dispose();

    phoneNumberFocusNode?.dispose();
    phoneNumberTextController?.dispose();

    numberOfGuestsFocusNode?.dispose();
    numberOfGuestsTextController?.dispose();

    messageFocusNode?.dispose();
    messageTextController?.dispose();
  }
}
