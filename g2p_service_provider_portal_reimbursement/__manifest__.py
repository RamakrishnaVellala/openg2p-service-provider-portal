{
    "name": "G2P Service Provider Portal: Reimbursement",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": ["g2p_program_reimbursement", "g2p_portal_base"],
    "data": [
        "data/g2p_service_provider_form_action_data.xml",
        "views/g2p_service_provider_form_template.xml",
        "views/g2p_service_provider_form_submitted.xml",
        "views/g2p_service_provider_reimbursement.xml",
        "views/g2p_service_provider_dashboard.xml",
        "views/base.xml",
        "views/home.xml",
        "views/login.xml",
        "views/profile.xml",
    ],
    "assets": {
        "website.assets_wysiwyg": [
            "g2p_service_provider_portal_reimbursement/static/src/js/reim_form_editor.js",
        ],
    },
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
