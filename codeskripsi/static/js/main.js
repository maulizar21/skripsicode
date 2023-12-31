
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
    var day = {0 : "Minggu", 1 : 'Senin', 2 : 'Selasa', 3 : 'Rabu', 4 : 'Kamis', 5 : 'Jumat', 6 : 'Sabtu'};
    var months = {
      0: 'Januari',
      1: 'Februari',
      2: 'Maret',
      3: 'April',
      4: 'Mei',
      5: 'Juni',
      6: 'Juli',
      7: 'Agustus',
      8: 'September',
      9: 'Oktober',
      10: 'November',
      11: 'Desember'
  };
    var hari_tgl = day[date.getDay()]+", "+date.getDate()+"-"+(months[date.getMonth()])+"-"+date.getFullYear();
    var menit = (date.getMinutes()<10 ? '0' : '')+date.getMinutes();
    var detik = (date.getSeconds()<10 ? '0' : '')+date.getSeconds();
    var jam = (date.getHours()<10 ? '0' : '')+date.getHours();
    var display = hari_tgl+", "+jam+":"+menit+":"+detik;
    $('#datetime-live').text(
        display
    );
}, 500);