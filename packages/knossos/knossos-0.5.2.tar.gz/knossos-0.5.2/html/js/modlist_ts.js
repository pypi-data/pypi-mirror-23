function get_translation_source() {
    var ts = [];
    function qsTr(k) { ts.push(k); }
    qsTr("\n                        <div class=\"container main-notice\">\n                            <h1>Welcome!</h1>\n                            \n                            <p>It looks like you started Knossos for the first time.</p>\n                            <p>You need to select a directoy where Knossos will store the game data (models, textures, etc.).</p>\n                            \n                            <form class=\"form-horizontal\">\n                                <div class=\"form-group\">\n                                    <div class=\"col-xs-8\">\n                                        <input type=\"text\" class=\"form-control\" v-model=\"data_path\">\n                                    ");
    return ts;
}
