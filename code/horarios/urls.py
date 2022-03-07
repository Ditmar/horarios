from django.conf.urls import patterns, include, url
from django.contrib import admin
from horarios.registros.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'horarios.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
 	url(r'^$', visuzarporDocente), 
 	url(r'^horas/$', getHorasDias),
 	url(r'^docente/$',porDocente),
 	url(r'^buscarDocente/$',buscarDocente),
 	#selectDocente
 	url(r'^selectDocente/(?P<id>\d+)/$',selectDocente),
 	#loadMateriap
 	url(r'^loadMateria/(?P<id>\d+)/$',loadMateria),
 	#loadSemestreHorario
 	url(r'^loadSemestreHorario/$',loadSemestreHorario),
 	#porSemestre
 	url(r'^porSemestre/$',porSemestre),
 	#loadHorarioMateria
 	url(r'^porAmbiente/(?P<id>\d+)/$',porAmbiente),
 	#getAmbiente
 	url(r'^getAmbiente/(?P<id>\d+)/$',getAmbiente),
 	#guardar
 	url(r'^guardar/$',guardar),
 	url(r'^borrarHorario/(?P<id>\d+)/$',borrarHorario),
 	url(r'^lista/$',ListaDocentes),
 	url(r'^loadSem/(?P<id>\d+)/$',loadSem),
 	url(r'^setSem/$',setSem),
 	#reporteSemestre
	url(r'^reporteSemestre/$',reporteSemestre),
	#porSemestreReporte
	url(r'^porSemestreReporte/(?P<id>\d+)/$',porSemestreReporte),
	#porDocenteReporte
	url(r'^porDocenteReporte/(?P<id>\d+)/$',porDocenteReporte),
	#reporteDocente
	url(r'^reporteDocente/$',reporteDocente),
	url(r'^reporteAmbiente/$',reporteAmbiente),
	#imprimirPlanilla
	url(r'^imprimir/$',imprimirPlanilla),
	url(r'^imprimir2/$',imprimirPlanilla2),
	#imprimirPlanilla2
	url(r'^estudiantes/$',imprimirPlanilla2),
	#plantilla JSON Materias
	url(r'^jsonmaterias/$',materiasjson),
	#updatemateria
	url(r'^updatemateria/$',updatemateria),
	#deletemateria
	url(r'^deletemateria/$',deletemateria)
)