[app]
title = Call Blocker
package.name = callblocker
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

android.permissions = READ_CONTACTS, READ_PHONE_STATE, ANSWER_PHONE_CALLS, MANAGE_OWN_CALLS, CALL_COMPANION_SERVICE

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
