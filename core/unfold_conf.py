from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Speaklish Dashboard",
    "SITE_HEADER": "Speaklish Dashboard",
    "SITE_URL": "https://www.speaklish.uz/",
    "SITE_ICON": {
        "light": lambda request: static("admin/img/favicon.svg"),  # light mode
        "dark": lambda request: static("admin/img/favicon.svg"),  # dark mode
    },
    "SITE_LOGO": {
        "light": lambda request: static("admin/img/favicon.svg"),  # light mode
        "dark": lambda request: static("admin/img/favicon.svg"),  # dark mode
    },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    "SHOW_HISTORY": True,  # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True,  # show/hide "View on site" button, default: True
    "ENVIRONMENT": "apps.common.views.environment_callback",
    # "DASHBOARD_CALLBACK": "apps.common.dashboard.dashboard_callback",
    "LOGIN": {
        "image": lambda request: static("admin/img/favicon.svg"),
    },
    "STYLES": [
        lambda request: static("assets/css/main.css"),
    ],
    "SCRIPTS": [
        lambda request: static("assets/js/admin.js"),
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    # "EXTENSIONS": {
    #     "modeltranslation": {
    #         "flags": {
    #             "uz": "🇺🇿",
    #             "ru": "🇷🇺",
    #             "en": "🇬🇧",
    #         },
    #     },
    # },
    "SIDEBAR": {
        "show_search": False,  # Search in applications and models names
        "show_all_applications": False,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Users"),
                "separator": True,
                "items": [
                    {
                        "title": _("Users"),
                        "icon": "people",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "groups",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
            {
                "title": _("Dashboard"),
                "separator": True,
                "items": [
                    {
                        "title": _("Organizations"),
                        "icon": "business",
                        "link": reverse_lazy("admin:dashboard_organization_changelist"),
                    },
                    {
                        "title": _("Groups"),
                        "icon": "groups_2",
                        "link": reverse_lazy("admin:dashboard_group_changelist"),
                    },
                    {
                        "title": _("Student Test Results"),
                        "icon": "assignment",
                        "link": reverse_lazy("admin:dashboard_studenttestresult_changelist"),
                    },
                ],
            },
        ],
    },
}
