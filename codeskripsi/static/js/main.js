
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

setInterval(function() {
    var jkt = new Date().toLocaleString("en-US", {timeZone: "Asia/Jakarta"});
    var date = new Date(jkt);
    var day = {1 : 'Senin', 2 : 'Selasa', 3 : 'Rabu', 4 : 'Kamis', 5 : 'Jumat', 6 : 'Sabtu', 7 : 'Minggu'};
    var hari_tgl = day[date.getDay()]+", "+date.getDate()+"-"+(date.getMonth()+1)+"-"+date.getFullYear();
    var menit = (date.getMinutes()<10 ? '0' : '')+date.getMinutes();
    var detik = (date.getSeconds()<10 ? '0' : '')+date.getSeconds();
    var jam = (date.getHours()<10 ? '0' : '')+date.getHours();
    var display = hari_tgl+", "+jam+":"+menit+":"+detik;
    $('#datetime-live').text(
        display
    );
}, 500);