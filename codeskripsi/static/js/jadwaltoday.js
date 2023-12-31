function absen(presence_url){
    const konfirmasi = confirm("Konfirmasi Kehadrian Kelas Ini?");
    console.log(presence_url)
    if(konfirmasi) {
        window.location.replace(presence_url)
    };

}