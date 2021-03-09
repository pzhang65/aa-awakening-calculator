(function (window, document, undefined) {
  const myForm = document.getElementById('myForm');
  //Enables popover everywhere on document
  var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
  var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl)
  })

  myForm.addEventListener('submit', function(e){
    e.preventDefault();

    //serialized data as a formdata object sent to calculate route
    const formData = new FormData(this);
    // returns a promise
    fetch('/calculate', {
      method : 'post',
      body : formData
    }).then(function (result){ // resolves to a response object
        return result.json();
    }).then(function (json){
      const sucAlert1 = document.getElementById('success_alert');
      const sucAlert2 = document.getElementById('success_alert2');
      const errAlert = document.getElementById('error_alert');

      const errors = document.querySelectorAll('.invalid-feedback');
      const awkError = document.getElementById('awk_error');
      const failError = document.getElementById('fail_error');
      const sucError = document.getElementById('suc_error');
      if (json.success){
        sucAlert1.innerText = json.message;
        sucAlert1.style.display = "block";

        sucAlert2.innerText = json.message2;
        sucAlert2.style.display = "block";

        // hide all error related content upon succesful validation
        errAlert.style.display = "none";
        errors.forEach(error => error.style.display = "none");

      } else {
        // hide all errors in case there are uncorrected error messages from last request
        errors.forEach(error => error.style.display = "none");

        for (let i = 0; i < json.key.length ; i++) {
          let f = json.key[i][0]+'Error';
          let text = json.key[i][1][0]; // Only need to display one error at a time
          eval(f).innerText = text;
          eval(f).style.display = "block";
        }
        errAlert.innerText = json.message;
        errAlert.style.display = "block";

        //hide success related content since not validated
        sucAlert1.style.display = "none";
        sucAlert2.style.display = "none";
      }
    })

  });
}(window, document));
