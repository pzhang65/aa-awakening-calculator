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


      if (json.success){
        const sucAlert1 = document.getElementById('success_alert');
        sucAlert1.innerText = json.message;
        sucAlert1.style.display = "block";

        const sucAlert2 = document.getElementById('success_alert2');
        sucAlert1.innerText = json.message2;
        sucAlert1.style.display = "block";
      }
    })

  });
}(window, document));
