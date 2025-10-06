import '/flutter_flow/flutter_flow_calendar.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/material.dart';
import 'booking_calendar_model.dart';
export 'booking_calendar_model.dart';

class BookingCalendarWidget extends StatefulWidget {
  const BookingCalendarWidget({super.key});

  @override
  State<BookingCalendarWidget> createState() => _BookingCalendarWidgetState();
}

class _BookingCalendarWidgetState extends State<BookingCalendarWidget> {
  late BookingCalendarModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => BookingCalendarModel());
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      width: MediaQuery.sizeOf(context).width * 1.0,
      height: MediaQuery.sizeOf(context).height * 0.8,
      decoration: BoxDecoration(
        color: FlutterFlowTheme.of(context).secondaryBackground,
      ),
      child: Align(
        alignment: AlignmentDirectional(0.0, -1.0),
        child: FlutterFlowCalendar(
          color: FlutterFlowTheme.of(context).primary,
          iconColor: FlutterFlowTheme.of(context).secondaryText,
          weekFormat: false,
          weekStartsMonday: false,
          rowHeight: 48.0,
          onChange: (DateTimeRange? newSelectedDate) async {
            if (_model.calendarSelectedDay == newSelectedDate) {
              return;
            }
            _model.calendarSelectedDay = newSelectedDate;
            FFAppState().selectedDate = _model.calendarSelectedDay?.start;
            _model.updatePage(() {});
            Navigator.pop(context);
            safeSetState(() {});
          },
          titleStyle: FlutterFlowTheme.of(context).titleLarge.override(
                fontFamily: FlutterFlowTheme.of(context).titleLargeFamily,
                letterSpacing: 0.0,
                useGoogleFonts:
                    !FlutterFlowTheme.of(context).titleLargeIsCustom,
              ),
          dayOfWeekStyle: FlutterFlowTheme.of(context).bodyLarge.override(
                fontFamily: FlutterFlowTheme.of(context).bodyLargeFamily,
                letterSpacing: 0.0,
                useGoogleFonts: !FlutterFlowTheme.of(context).bodyLargeIsCustom,
              ),
          dateStyle: FlutterFlowTheme.of(context).bodyMedium.override(
                fontFamily: FlutterFlowTheme.of(context).bodyMediumFamily,
                letterSpacing: 0.0,
                useGoogleFonts:
                    !FlutterFlowTheme.of(context).bodyMediumIsCustom,
              ),
          selectedDateStyle: FlutterFlowTheme.of(context).titleSmall.override(
                fontFamily: FlutterFlowTheme.of(context).titleSmallFamily,
                letterSpacing: 0.0,
                useGoogleFonts:
                    !FlutterFlowTheme.of(context).titleSmallIsCustom,
              ),
          inactiveDateStyle: FlutterFlowTheme.of(context).labelMedium.override(
                fontFamily: FlutterFlowTheme.of(context).labelMediumFamily,
                letterSpacing: 0.0,
                useGoogleFonts:
                    !FlutterFlowTheme.of(context).labelMediumIsCustom,
              ),
          locale: FFLocalizations.of(context).languageCode,
        ),
      ),
    );
  }
}
