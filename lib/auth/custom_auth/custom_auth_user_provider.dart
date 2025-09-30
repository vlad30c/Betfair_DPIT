import 'package:rxdart/rxdart.dart';

import '/backend/schema/structs/index.dart';
import 'custom_auth_manager.dart';

class BiteAuthUser {
  BiteAuthUser({
    required this.loggedIn,
    this.uid,
    this.userData,
  });

  bool loggedIn;
  String? uid;
  UserStruct? userData;
}

/// Generates a stream of the authenticated user.
BehaviorSubject<BiteAuthUser> biteAuthUserSubject =
    BehaviorSubject.seeded(BiteAuthUser(loggedIn: false));
Stream<BiteAuthUser> biteAuthUserStream() =>
    biteAuthUserSubject.asBroadcastStream().map((user) => currentUser = user);
