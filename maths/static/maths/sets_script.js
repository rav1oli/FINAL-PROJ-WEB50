function render_sets(sets) {

    const template = $('#sets-template').html();
    const rendered = Mustache.render(template, sets);
    $('.problem-sets').html(rendered);
    
}