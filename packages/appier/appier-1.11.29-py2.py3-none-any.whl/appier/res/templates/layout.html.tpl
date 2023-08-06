<!DOCTYPE html>
<html lang="en">
    <head>
        {% block head %}
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
            <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, minimum-scale=1, maximum-scale=1" />
            <link rel="stylesheet" type="text/css" href="{{ url_for('appier', filename = 'css/base.css') }}" />
            <link rel="shortcut icon" href="{{ url_for('appier', filename = 'images/favicon.ico') }}" />
            <script type="text/javascript" src="{{ url_for('appier', filename = 'js/base.js') }}"></script>
            <title>{% block title %}{% endblock %}</title>
        {% endblock %}
    </head>
    <body>
        <div id="header" class="header">
            {% block header %}{% endblock %}
        </div>
        <div id="content" class="content">
            {% block content %}{% endblock %}
        </div>
        <div id="footer" class="footer">
            {% block footer %}
                Brought to you by <a href="http://hive.pt">Hive Solutions</a> using
                <a href="http://appier.hive.pt">Appier Framework</a>.
                {% if own and own.is_devel() %}
                    <br/>
                    {{ own.info_dict().identifier }}
                    {{ own.info_dict().server_full }}
                {% endif %}
            {% endblock %}
        </div>
    </body>
</html>
