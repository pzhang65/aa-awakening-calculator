(function ($, window, document) {

  $(document).ready(function () {
    var myForm = $('#myForm');
    //Enables popover everywhere on document
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
      return new bootstrap.Popover(popoverTriggerEl)
    })

    myForm.on('submit', function (e) {
      e.preventDefault();
      var data = myForm.serialize();

      $.post('/calculate', data, function (result) {
        if (result.success) {
          $('#success_alert').text(result.message).show();
          $('#success_alert2').text(result.message2).show();
          // hide all error related content upon succesful validation
          $('#error_alert').hide();
          $('#awk_error').hide();
          $('#fail_error').hide();
          $('#suc_error').hide();
        } else {
          // hide all errors in case there are uncorrected error messages from last POST
          $('#awk_error').hide();
          $('#fail_error').hide();
          $('#suc_error').hide();
          // iterate through errors in err_key
          $.each(result.key, function (index, value) {
            // show only the first error in errorMessages
            // because NumberRange() is in the domain of IntegerField()
            $('#'+value[0]+'_error').text(value[1][0]).show()
          });
          $('#error_alert').text(result.message).show();
          //hide success related content since not validated
          $('#success_alert').hide();
          $('#success_alert2').hide();
        }
        console.log(result);
      });
    })
  });
}(jQuery, window, document))
