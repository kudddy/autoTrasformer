from random import choice

headers_auto_ru = {
    "Content-Type": "application/json",
    "Cookie": "autoru_gdpr=1; X-Vertis-DC=vla; _ym_d=1628595663; _ym_uid=1628595552586528384; from=direct; from_lifetime=1628595663514; cycada=E4Yk+1cDWoiYP5LaxJly34YqcwM/ywaWEp8N9/2VJNI=; _ym_isad=2; gdpr=0; yandexuid=9622985041628595547; yuidlt=1; _csrf_token=0e0b308743aa8800b98ebad40b843910f75fafccb7e0e6a0; autoru_sid=a%3Ag6112655b2odv0c7jcqfuc8s4arr4f65.6ea0814456efdff360711066f12bb9a1%7C1628595547452.604800.5edZtFDHuX2GcmrLddlxsg.YGak3Ukh3Km-pltAs48T9VzysP1h5ibi2CVXfYvpPGI; autoruuid=g6112655b2odv0c7jcqfuc8s4arr4f65.6ea0814456efdff360711066f12bb9a1; suid=3eee3e3d65f09eb42a6f941b192f5d37.046c4474ea8297031f03061dafecdc0c",
    "x-client-date": "1628595665225",
    "x-requested-with": "fetch",
    "x-page-request-id": "e8217efbaa83676bdf1403e577b1be73",
    "x-client-app-version": "b4d66ad3005",
    "x-csrf-token": "0e0b308743aa8800b98ebad40b843910f75fafccb7e0e6a0",
    "Connection": "keep-alive",
    "Referer": "https://auto.ru/",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Origin": "https://auto.ru"
}


def mixer_headers_auto_ru():
    """Микс хедеров живых пользователей для размытия нагрузки на сервис"""
    return choice([
        {
            "Content-Type": "application/json",
            "Cookie": "autoru_gdpr=1; X-Vertis-DC=sas; _ym_d=1629447955; _ym_uid=1629447939409175437; from=direct; from_lifetime=1629447955427; _ym_isad=2; gdpr=0; _csrf_token=b468bf83bfe8143462bc180e6d93246ad832f0a2583e4726; autoru_sid=a%3Ag611f66fe2egkn59s0pidp1bv39k24fe.f3ec7e3dadc51ab04ce2fbdde29d3229%7C1629447934125.604800.V79KEbXPMNDyXk4rcyk5sg.mi_G3stHpCQYLkw5F8762EjrMNJAzpBpuj3v2OiQQBY; autoruuid=g611f66fe2egkn59s0pidp1bv39k24fe.f3ec7e3dadc51ab04ce2fbdde29d3229; suid=c33f8eb8fb44c902707fda4e1b747b2a.80a3bf19385226ae48ccdaa78d77af0d; yandexuid=4246932261629447934; yuidlt=1",
            "x-client-date": "1629447956280",
            "x-requested-with": "fetch",
            "x-page-request-id": "f80b26979625f3a94250e19d41015be6",
            "x-client-app-version": "0402a27770a",
            "x-csrf-token": "b468bf83bfe8143462bc180e6d93246ad832f0a2583e4726",
            "Connection": "keep-alive",
            "Referer": "https://auto.ru/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Origin": "https://auto.ru"
        },
        {
            "Content-Type": "application/json",
            "Cookie": "autoru_gdpr=1; X-Vertis-DC=vla; _ym_d=1629448222; _ym_uid=162944817634863142; from=direct; from_lifetime=1629448222638; _ym_isad=2; gdpr=0; _csrf_token=aa9e5cfb95f4ea85ce60e5f15936951f3dfd42b3720e3caf; autoru_sid=a%3Ag611f67eb2h961tsvn02g5f3tu8ti4ms.632abdeb0f1e41e2811495d72fa7c14d%7C1629448171298.604800.6s_3-9biTo18svsyf1XP-A.c4o5efkViKrDh69pJA4mql1gIysJ6V8WpKQuLNdmkY0; autoruuid=g611f67eb2h961tsvn02g5f3tu8ti4ms.632abdeb0f1e41e2811495d72fa7c14d; suid=9a5fa9d08e7aceadefc7b629130c178a.3c511935bc630114b0445a7cd47b16b4; yandexuid=4409445711629448171; yuidlt=1",
            "x-client-date": "1629448223051",
            "x-requested-with": "fetch",
            "x-page-request-id": "ad6462dfd228c078502be9204a83aba3",
            "x-client-app-version": "0402a27770a",
            "x-csrf-token": "aa9e5cfb95f4ea85ce60e5f15936951f3dfd42b3720e3caf",
            "Connection": "keep-alive",
            "Referer": "https://auto.ru/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Origin": "https://auto.ru"
        },
        {
            "Content-Type": "application/json",
            "Cookie": "autoru_gdpr=1; X-Vertis-DC=sas; _ym_d=1629448317; _ym_uid=162944830946908368; from=direct; from_lifetime=1629448317276; _ym_isad=2; gdpr=0; counter_ga_all7=2; _csrf_token=33ebfd0dd99a66618686c2910bdd23f99b4ca54699366b9d; autoru_sid=a%3Ag611f68702g4kr2t6l3br5du2hjv1g7r.4617ff083f998551eb72983a9b158e2e%7C1629448304134.604800.k_IsECkGdrNtOJj-uLUzSg.d1szILpLTPnNgYNNas98Ob1mr32-l1ddp-pKK9ZFlLk; autoruuid=g611f68702g4kr2t6l3br5du2hjv1g7r.4617ff083f998551eb72983a9b158e2e; suid=4464722ea8f639a4c8573e6b79336bd4.3c33bf354fa9e8c8c91977cc531278a0; yandexuid=8286786911629448304; yuidlt=1X-Vertis-DC=sas; _ym_d=1629448317; _ym_uid=162944830946908368; from=direct; from_lifetime=1629448317276; _ym_isad=2; gdpr=0; counter_ga_all7=2; _csrf_token=33ebfd0dd99a66618686c2910bdd23f99b4ca54699366b9d; autoru_sid=a%3Ag611f68702g4kr2t6l3br5du2hjv1g7r.4617ff083f998551eb72983a9b158e2e%7C1629448304134.604800.k_IsECkGdrNtOJj-uLUzSg.d1szILpLTPnNgYNNas98Ob1mr32-l1ddp-pKK9ZFlLk; autoruuid=g611f68702g4kr2t6l3br5du2hjv1g7r.4617ff083f998551eb72983a9b158e2e; suid=4464722ea8f639a4c8573e6b79336bd4.3c33bf354fa9e8c8c91977cc531278a0; yandexuid=8286786911629448304; yuidlt=1",
            "x-client-date": "1629448317643",
            "x-requested-with": "fetch",
            "x-page-request-id": "b6a9443a87075a800244940ae9c0b0d9",
            "x-client-app-version": "0402a27770a",
            "x-csrf-token": "33ebfd0dd99a66618686c2910bdd23f99b4ca54699366b9d",
            "Connection": "keep-alive",
            "Referer": "https://auto.ru/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Origin": "https://auto.ru"
        },
        {
            "Content-Type": "application/json",
            "Cookie": "autoru_gdpr=1; X-Vertis-DC=vla; _ym_d=1629448476; _ym_uid=162944845892770554; from=direct; from_lifetime=1629448476940; _ym_isad=2; gdpr=0; _csrf_token=a54f2b378a8a3204c77c7c929f61d89f35dcd050cc4f9221; autoru_sid=a%3Ag611f69062bo8gg0p10u58rpep5cie4d.7c657e53e200395483204d03251f6cf2%7C1629448454665.604800.zRNAh37zOpvImuNPOcyvew.RDZDWMmcNRTOGMht7qfP-5dTgTSjOkFRvFTlsLBtfn8; autoruuid=g611f69062bo8gg0p10u58rpep5cie4d.7c657e53e200395483204d03251f6cf2; suid=2d137cbf3292a21730d280ee5fb1acbf.12aeef081edf242b593246b3744484ac; yandexuid=4669497581629448454; yuidlt=1",
            "x-client-date": "1629448478928",
            "x-requested-with": "fetch",
            "x-page-request-id": "f42175b5f5d581f5530ac7a6177c1047",
            "x-client-app-version": "0402a27770a",
            "x-csrf-token": "a54f2b378a8a3204c77c7c929f61d89f35dcd050cc4f9221",
            "Connection": "keep-alive",
            "Referer": "https://auto.ru/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Origin": "https://auto.ru"
        },
        {
            "Content-Type": "application/json",
            "Cookie": "autoru_gdpr=1; X-Vertis-DC=vla; _ym_d=1628595663; _ym_uid=1628595552586528384; from=direct; from_lifetime=1628595663514; cycada=E4Yk+1cDWoiYP5LaxJly34YqcwM/ywaWEp8N9/2VJNI=; _ym_isad=2; gdpr=0; yandexuid=9622985041628595547; yuidlt=1; _csrf_token=0e0b308743aa8800b98ebad40b843910f75fafccb7e0e6a0; autoru_sid=a%3Ag6112655b2odv0c7jcqfuc8s4arr4f65.6ea0814456efdff360711066f12bb9a1%7C1628595547452.604800.5edZtFDHuX2GcmrLddlxsg.YGak3Ukh3Km-pltAs48T9VzysP1h5ibi2CVXfYvpPGI; autoruuid=g6112655b2odv0c7jcqfuc8s4arr4f65.6ea0814456efdff360711066f12bb9a1; suid=3eee3e3d65f09eb42a6f941b192f5d37.046c4474ea8297031f03061dafecdc0c",
            "x-client-date": "1628595665225",
            "x-requested-with": "fetch",
            "x-page-request-id": "e8217efbaa83676bdf1403e577b1be73",
            "x-client-app-version": "b4d66ad3005",
            "x-csrf-token": "0e0b308743aa8800b98ebad40b843910f75fafccb7e0e6a0",
            "Connection": "keep-alive",
            "Referer": "https://auto.ru/",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
            "Origin": "https://auto.ru"
        }

    ])



headers_sberauto = {
    "Content-Type": "application/json"
}
