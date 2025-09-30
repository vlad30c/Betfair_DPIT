import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyDNnoAVP-APS2SoAoE0EhlWCFVkCDOq4hA",
            authDomain: "ceva-ceva-wmi3fb.firebaseapp.com",
            projectId: "ceva-ceva-wmi3fb",
            storageBucket: "ceva-ceva-wmi3fb.firebasestorage.app",
            messagingSenderId: "357980535788",
            appId: "1:357980535788:web:5e3f8dbf71430969765ec9",
            measurementId: "G-PLQYYN2VH1"));
  } else {
    await Firebase.initializeApp();
  }
}
