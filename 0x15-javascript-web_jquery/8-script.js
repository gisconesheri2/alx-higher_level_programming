$(function()
{
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
    function( resp ) {
        $.each( resp.results, function (index, movie)
        {
            $('ul#list_movies').append('<li>'+movie.title+'</li>');
        });
    });
});