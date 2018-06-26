var check = function() {
    if (document.getElementById('pass').value ==
      document.getElementById('cpass').value) {
      document.getElementById('message').style.color = 'green';
      document.getElementById('message').innerHTML = 'Matching &#9745;';
    } else {
      document.getElementById('message').style.color = 'red';
      document.getElementById('message').innerHTML = 'Not matching &#9746;';
    }
  }
  
