/* Handle the display of problem sets and such in sets.html */
$(document).ready(function(){

    const order = $('#order-selector').find(':selected').val();

    $('#public-sets').click(() => {load_sets("public", order)});

    load_sets("public", "-time_created"); // by default, load public sets

})

function load_sets(public, order){

    if (!(public === "public" || public === "my_sets")){
        console.log("error, must query for a valid subgroup of problem sets");
    }

    $.ajax({
        url: `sets/public/${order}`,
        type: 'GET',

        success: function(response){
            console.log(JSON.stringify(response, 0, 2))
            render_sets({'sets': response.sets}); /* in sets_script.js */
        },
        error: function(){
            console.log("error");
        }
    });

}
