register_check_parameters(
    subgroup_environment,
    "liebertCRV_air_temp",
    _("Air Temperature for Liebert CRV"),
    Dictionary(
        elements = [
            ("allAisle_levels",
                Tuple(
                    title = _("Low and High Warning/Critical Levels"),
                    elements = [
                        Float(title = _("Critical if below"), default_value = 15),
                        Float(title = _("Warning if below"), default_value = 17),
                        Float(title = _("Warning if above"), default_value = 25),
                        Float(title = _("Critical if above"), default_value = 27),
                    ],
                    help = _("1) Please specify service these parameters apply to below, otherwise they will affect BOTH Hot and Cold Aisle Temperature services<br>2) Note: Data return from CRV is limited to 1 decimal point, further significance will be truncated.")
                )
            )
        ]
    ),
    TextAscii(
        title = _("Service: "),
        help = _("As return and supply temperature services are separate, select the appropriate service relevant to the parameters applied."),
    ),
    "dict"
)
