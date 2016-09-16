// AJAX for posting
function catogorise_post(form) {
    $form = form
    $.ajax({
        url : $form.attr('action'), // the endpoint
        type : "POST", // http method
        data : { 
            category : $form.children().find("select :selected").val(),
            csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
        }, // data sent with the post request
        // handle a successful response
        success : function(data) {
            $($form.attr('id')).val(''); // remove the value from the input
            console.log(data); // log the returned data to the console
            console.log("success"); // another sanity check
            $form.siblings('.category-field').text($form.children().find("select :selected").text());
            $.notify({
                icon: data['icon'],
                message: "<b>" + data['message'] + "</b>"
            },{
                type: data['type'],
                timer: 500
            });
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
    console.log(form);
};