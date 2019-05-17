$.get('https://swapi.co/api/films/?format=json', function (r) {
  let movies = r.results;
  for (let i = 0; i < movies.length; i++) {
    $('#list_movies').append('<li>' + movies[i].title + '</li>');
  }
});
