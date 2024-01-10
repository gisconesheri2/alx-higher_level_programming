$(function()
{
    $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function( resp ) {
        $('div#character').text(resp.name);
    });
});