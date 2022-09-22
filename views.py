from django.http import HttpResponse
from django.shortcuts import render


def gestion_medica(request):

    return render(request,"gestion_medica.html")


def gestion_medica_registrar(request):
    frecuencia = request.GET["frecuencia"]
    saturacion = request.GET["saturacion"]
    stress = request.GET["stress"]
    nombre = request.GET["nombre"]
    apellido = request.GET["apellido"]
    edad = request.GET["edad"]
    peso = request.GET["peso"]

    html = """
    <html>
        <body>
            <table border="1" cellspacing="3" cellpadding="1" width="100%">
            <tr>
                <td><b>Frecuencia Cardiaca: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Saturacion en la Sangre: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Nivel de Stress: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Nombre: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Apellido: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Edad: </b></td>
                <td>%s</td>
            </tr>
            <tr>
                <td><b>Peso: </b></td>
                <td>%s</td>
            </tr>            
            </table>
        </body>
    </html>
    """

    return HttpResponse(html)
