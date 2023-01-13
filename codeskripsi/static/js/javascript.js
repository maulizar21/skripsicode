var cameraModal = new bootstrap.Modal(document.getElementById('cameraModal'), {
  keyboard: false
})
let video = document.querySelector("#video");
let submit_login_form = document.querySelector("#submit-login-form");
let canvas = document.querySelector("#canvas");
let stream;
var nav_open = false;


function toggleNav(){
  if(!nav_open){  
    openNav()
  }else {
    closeNav()
  }
  nav_open= !nav_open
}
function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  }

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
  }

$("#openCameraModal").click(async function(){
  if ('mediaDevices' in navigator && 'getUserMedia' in navigator.mediaDevices) {
    cameraModal.show()
  }else{
    return alert("perangkatn anda tidak support")
  }
  let constraints = { 
    video: true, audio: false
};
  stream = await navigator.mediaDevices.getUserMedia(constraints);
	video.srcObject = stream;
  let stream_settings = stream.getVideoTracks()[0].getSettings();
  console.log(stream_settings.width, stream_settings.height);
  canvas.height = stream_settings.height;
  canvas.width = stream_settings.width;
})

$("#submit-login-form").click(function() {
  console.log(canvas.width, canvas.height)
  console.log(video)
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width,canvas.height );
  let image_data_url = canvas.toDataURL('image/jpeg');

  // data url of the image

  let value = $("#form-login").serializeArray();

  let form_data = {
    csrfmiddlewaretoken : value[0].value,
    camera_data : image_data_url,
    username : value[1].value,
    password : value[2].value,
  }
  console.log(value)
  console.log(form_data);

  const formData = new FormData(document.getElementById("form-login"));
  formData.append("camera_data", image_data_url)
  for (const pair of formData.entries()) {
    console.log(`${pair[0]}, ${pair[1]}`);
  }

  $("#loading-spinner").removeClass("d-none")
  $.ajax({
    url: '/login',
    data: formData,
    processData: false,
    contentType: false,
    type: 'POST',
    success: function(data){
      $("#login-alert").removeClass("alert-primary alert-danger")
      $("#login-alert").addClass(data.status ? "alert-primary" : "alert-danger")
      $("#login-alert").text(data.message)
      $("#login-alert").removeClass("d-none")

      if(data.status){
        window.location.href = '/'
        $("#loading-spinner").addClass("d-none")
        // alert(data.message)
      }else{
        $("#loading-spinner").addClass("d-none")
        // alert(data.message)
      }
    }
  });

});

$("#cameraModal .btn-close").click(function(){
  cameraModal.hide()
  stream.getTracks().forEach(track => track.stop())
})

setInterval(function() {
    var jkt = new Date().toLocaleString("en-US", {timeZone: "Asia/Jakarta"});
    var date = new Date(jkt);
    var day = {1 : 'Senin', 2 : 'Selasa', 3 : 'Rabu', 4 : 'Kamis', 5 : 'Jumat', 6 : 'Sabtu', 7 : 'Minggu'};
    var hari_tgl = day[date.getDay()]+", "+date.getDate()+"-"+(date.getMonth()+1)+"-"+date.getFullYear();
    var menit = (date.getMinutes()<10 ? '0' : '')+date.getMinutes();
    var detik = (date.getSeconds()<10 ? '0' : '')+date.getSeconds();
    var jam = (date.getHours()<10 ? '0' : '')+date.getHours();
    var display = hari_tgl+", "+jam+":"+menit+":"+detik;
    console.log(display)
    // $('#datetime-live').html(
    //     display
    // );
}, 500);