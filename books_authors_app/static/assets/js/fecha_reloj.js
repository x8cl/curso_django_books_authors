$(document).ready(function(){

    FechaHora();
    setInterval(FechaHora, 1000);

    function FechaHora(){
        var nombres_dias = new Array("Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado")
        var nombres_meses = new Array("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

        var momentoActual = new Date()
        var hora = momentoActual.getHours()
        var minuto = momentoActual.getMinutes()
        var segundo = momentoActual.getSeconds()

        if (hora < 10) hora = 0 + hora;
        if (minuto < 10) minuto = "0" + minuto;
        if (segundo < 10) segundo = "0" + segundo;

        var horaImprimible = hora + ":" + minuto + ":" + segundo

        var dia = momentoActual.getDate()
        var dia_semana = momentoActual.getDay()
        var mes = momentoActual.getMonth()
        var anio = momentoActual.getFullYear()

        var fecha_actual  = nombres_dias[dia_semana] +", "+ dia +" de "+ nombres_meses[mes] +" de "+ anio

        $("#HoraActual").text(fecha_actual + " | " + horaImprimible);

    }

});