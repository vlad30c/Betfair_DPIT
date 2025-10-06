import '/flutter_flow/flutter_flow_google_map.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'restaurant_interface_map_widget.dart' show RestaurantInterfaceMapWidget;
import 'package:flutter/material.dart';

class RestaurantInterfaceMapModel
    extends FlutterFlowModel<RestaurantInterfaceMapWidget> {
  ///  State fields for stateful widgets in this page.

  // State field(s) for GoogleMap widget.
  LatLng? googleMapsCenter;
  final googleMapsController = Completer<GoogleMapController>();

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {}
}
