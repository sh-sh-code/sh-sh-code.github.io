# Nagi Lab site (https://sh-sh-code.github.io)

Developer website for Nagi Lab apps. Hosts app-ads.txt (must stay at the domain root) and each app's legal pages.

| URL | Purpose |
|---|---|
| `/app-ads.txt` | Authorized ad sellers. Add the AppLovin MAX lines when the account is approved (MAX dashboard generates them). |
| `/support/` | Public contact (email pending: a dedicated Nagi Lab address the owner is creating) |
| `/hima/privacy/` | HIMA privacy policy |
| `/hima/terms/` | HIMA terms of use |
| `/hima/delete-account/` | HIMA account deletion (Google Play requires a web URL) |

## Keep in sync with the app (before release)
- The pages describe the planned behavior of HIMA. Before release, the app must match them:
  in-app deletion at My Page -> "アカウント削除", deleted sender shown as "退会したユーザー",
  email deletion requests completed within 30 days, the SDK list in privacy section 4.
- Any new SDK or data type in HIMA -> update `/hima/privacy/` and the Play Data safety form together.
- Contact email: replace every `class="contact-email"` span.
- The game's privacy policy is added at its release gate (BL-32), after the SDK set is final.
- Final legal review is done by the owner before release.
