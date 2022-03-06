from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from .models import *
import json
from django.db.models import Q
from .forms import *
import pdb
# Create your views here.

def setMaterias():
	data=[
	{'sigla':"LIN 181 ",'nombre':"INGLES 1"},
	{'sigla':"SIS-131",'nombre':"TECNICAS DE PROGRAMACION 1"},
	{'sigla':"MAT-180",'nombre':"FUNDAMENTOS DE INVESTIGACION"},
	{'sigla':"SIS-100",'nombre':"ALGEBRA"},
	{'sigla':"MAT-101",'nombre':"CALCULO 1"},
	{'sigla':"FIS 100",'nombre':"FISICA 1"},
	{'sigla':"MAT-221",'nombre':"ESTADISTICA 1"},
	{'sigla':"LIN-282",'nombre':"INGLES 2"},
	{'sigla':"MAT-102",'nombre':"CALCULO 2"},
	{'sigla':"MAT-103",'nombre':"ALGEBRA LINEAL Y TEORIA MATRICIAL"},
	{'sigla':"FIS-201",'nombre':"FISICA 2"},
	{'sigla':"SIS-233",'nombre':"DISENO COMPUTARIZADO"},
	{'sigla':"MAT-322",'nombre':"ESTADISTICA 2"},
	{'sigla':"LIN-383",'nombre':"INGLES 3"},
	{'sigla':"Sis-334",'nombre':"ESTRUCTURAS DE DATOS"},
	{'sigla':"MAT-207",'nombre':"CALCULO 3"},
	{'sigla':"FIS-302",'nombre':"FISICA 3"},
	{'sigla':"SIS-311",'nombre':"SISTEMAS CONTABLES"},
	{'sigla':"SIS-401",'nombre':"CALCULO NUMERICO 1"},
	{'sigla':"SIS-402",'nombre':"ANLISIS DISCRETO"},
	{'sigla':"SIS-441",'nombre':"SISTEMAS ANLOGICOS Y DIGITALES"},
	{'sigla':"SIS-434",'nombre':"SEMINARIO DE PROGRAMCION"},
	{'sigla':"SIS-451",'nombre':"BASE DE DATOS 1"},
	{'sigla':"SIS-452",'nombre':"ANALISIS DE SISTEMAS 1"},
	{'sigla':"SIS-553",'nombre':"BASE DE DATOS 2"},
	{'sigla':"SIS-552",'nombre':"ANALISIS DE SISTEMAS 2"},
	{'sigla':"SIS-523",'nombre':"INVESTIGACION OPERATIVA 1"},
	{'sigla':"SIS-581",'nombre':"METODOLOGIA DE LA INVESTIGACION"},
	{'sigla':"SIS-556",'nombre':"SISTEMAS OPERATIVOS"},
	{'sigla':"SIS-555",'nombre':"ARQUITECTURA DE COMPUTADORES"},
	{'sigla':"SIS-624",'nombre':"INVESTIGACION OPERATIVA 2"},
	{'sigla':"SIS-657",'nombre':"AUDITORIA DE SISTEMAS"},
	{'sigla':"SIS-661",'nombre':"REDES"},
	{'sigla':"SIS-671",'nombre':"MODELOS ADMINISTRATIVOS"},
	{'sigla':"SIS-672",'nombre':"MODELOS ECONOMICOS"},
	{'sigla':"SIS-654",'nombre':"INGENIERIA DE SOFTWARE"},
	{'sigla':"SIS-131",'nombre':"TECNICAS DE PROGRAMACION 1"},
	{'sigla':"SIS-725",'nombre':"SIMULACION DE SISTEMAS"},
	{'sigla':"SIS-762",'nombre':"AUTOMATAS"},
	{'sigla':"SIS-758",'nombre':"SEMINARIO DE SISTEMAS"},
	{'sigla':"SIS-773",'nombre':"INGENIERIA DE SISTEMAS"},
	{'sigla':"SIS-774",'nombre':"PREPRACION Y EVALAUCION DE PROYECTOS"},
	{'sigla':"SIS-863",'nombre':"INTELIGENCIA ARTIFICIAL"},
	{'sigla':"SIS-864",'nombre':"TEORIA DE CONTROL"},
	{'sigla':"SIS-826",'nombre':"MODELADO DINAMICO DE SISTEMAS"},
	{'sigla':"SIS-859",'nombre':"SEMINAIRIO DE TESIS 1"},
	{'sigla':"SIS-998",'nombre':"PRACTICA LABORAL"},
	{'sigla':"SIS-999",'nombre':"SEMINARIO DE TESIS 2"}
	]
	#for i in range(1,10):
	#	nombre="Semestre %s"%(i)
	#	p=Semestres()
	#	p.nombre=nombre
	#	p.save()
	for i in data:
		p=Materia()
		p.sigla=i["sigla"]
		j=int(p.sigla[4])+36
		p.nombre=i["nombre"]
		p.semestre=Semestres.objects.get(pk=j)
		p.save()
def setHoras():
	for i in range(0,5):
		hora=7
		minutos=0		
		for j in range(0,19):
			p=Horarios()
			p.dia=i
			p.hora=hora
			p.minutos=minutos
			p.save()
			if(minutos+45>59):
				minutos=(minutos+45)%60
				hora=hora+1
				if hora==14:
					minutos=0
			else:
				minutos=minutos+45
class Horas():
	h=0
	m=0
def getHora(i):
	i=int(i)
	m=0
	h=7
	min_m=45
	ins=Horas()
	if i<9:
		for r in range(0,i):
			if m+45>59:
				h=h+1
			m=(m+45)%60
		ins.h=h
		ins.m=m
		return ins
	else:
		minutos=0
		m=0
		h=14
		min_m=0
		for r in range(9,i):
			if m+45>59:
				h=h+1
			m=(m+45)%60
		ins.h=h
		ins.m=m
		return ins
	return ins
def getHorasDias(request):
	horas=Horarios.objects.all()[0:18]
	data=[]
	for i in horas:
		aux="%s:%s" %(i.hora,i.minutos)
		data.append(aux)
	return HttpResponse(json.dumps(data),content_type="application/json")
def deleteHoras():
	d=Horarios.objects.all()
	d.delete()
def deleteMaterias():
	d=Materia.objects.all()
	d.delete()
def porDocente(request):
	doc=Docente.objects.get(pk=request.session["idDoc"])
	#sem=Semestres.objects.get(pk=1)
	horario=relacion.objects.filter(docentes=doc)
	horas=[]
	for i in horario:
		horas.append({"descripcion":"%s %s %s %s"%(i.materia.nombre,i.materia.sigla,i.docentes.nombre,i.docentes.apellido),"materia":"%s %s"%(i.materia,i.ambientes),"fila":"%s"%(i.fila),"columna":"%s"%(i.columna),"id":"%s"%(i.id)})
	return HttpResponse(json.dumps(horas),content_type="application/json")
def setSem(request):
	data={}
	data["code"]=False
	if(request.method=="POST"):
		form=Filter(request.POST)
		if( form.is_valid):
			request.session["code"]=request.POST["code"]
			data["code"]=request.session["code"]
			return HttpResponse(json.dumps(data),content_type="application/json")
	return HttpResponse(json.dumps(data),content_type="application/json")
def porSemestre(request):
	sem=Semestres.objects.get(pk=request.session["idSem"])
	#horario=relacion.objects.filter(semestre=sem,materia__sigla__contains="G3")
	if(request.session["code"]!=""):
		horario=relacion.objects.filter(semestre=sem,materia__sigla__contains=request.session["code"])
	else:
		horario=relacion.objects.filter(semestre=sem)
	horas=[]
	for i in horario:
		horas.append({"descripcion":"%s %s %s %s"%(i.materia.nombre,i.materia.sigla,i.docentes.nombre,i.docentes.apellido),"materia":"%s %s"%(i.materia,i.ambientes),"fila":"%s"%(i.fila),"columna":"%s"%(i.columna),"id":"%s"%(i.id)})
	return HttpResponse(json.dumps(horas),content_type="application/json")
def porAmbiente(request,id):
	amb=Ambientes.objects.get(pk=id)
	horario=relacion.objects.filter(ambientes=amb)
	horas=[]
	for i in horario:
		horas.append({"descripcion":"%s %s %s %s"%(i.materia.nombre,i.materia.sigla,i.docentes.nombre,i.docentes.apellido),"materia":"%s %s"%(i.materia,i.ambientes),"fila":"%s"%(i.fila),"columna":"%s"%(i.columna),"id":"%s"%(i.id)})
	return HttpResponse(json.dumps(horas),content_type="application/json")
def buscarDocente(request):
	if(request.method=="POST"):
		buscar=buscarDocenteForm(request.POST)
		if(buscar.is_valid()):
			#print buscar
			criterio=request.POST["buscar_docente"]
			lista=list(Docente.objects.filter(Q(nombre__contains=criterio)))
			if(len(lista)>0):
				return render_to_response("resultadosbusqueda.html",{"lista":lista},RequestContext(request))
			else:
				return render_to_response("noresultados.html",{"msn":"Resultados no Encontrados"},RequestContext(request))
		else:
			return render_to_response("noresultados.html",{"msn":""},RequestContext(request))
	return render_to_response("noresultados.html",{"msn":"Busqueda"},RequestContext(request))
def selectDocente(request,id):
	doc=Docente.objects.get(pk=id)
	request.session["idDoc"]=doc.id
	return render_to_response("selectDocente.html",{"doc":doc},RequestContext(request))
def visuzarporDocente(request):
	#setHoras()
	#setMaterias()
	#deleteHoras()
	#deleteMaterias()
	request.session["code"]=""
	form=buscarDocenteForm()
	amb=Ambientes.objects.all()
	semestre=Semestres.objects.all()
	ij=i_j()
	filtrar=Filter()
	return render_to_response("docente.html",{'filtrar':filtrar,'form':form,'ambientes':amb,'i_j':ij,"semestre":semestre},RequestContext(request))
#carga materias y el horario del semestre
def loadMateria(request,id):
	mat=Materia.objects.get(pk=id)
	request.session["idSem"]=mat.semestre.id
	request.session["idMat"]=mat.id
	return render_to_response("loadMateria.html",{"mat":mat},RequestContext(request))
def loadSemestreHorario(request):
	semestre=Semestres.objects.get(pk=request.session["idSem"])
	return render_to_response("loadHorario.html",{"semestre":semestre},RequestContext(request))
def getAmbiente(request,id):
	amb=Ambientes.objects.get(pk=id)
	request.session["idAmb"]=id
	return render_to_response("loadAmbiente.html",{"amb":amb},RequestContext(request))
def guardar(request):
	data={}
	data["response"]=False
	if(request.method=="POST"):
		formData=i_j(request.POST)
		if(formData.is_valid()):
			#pdb.set_trace()
			i=request.POST["i"]
			j=request.POST["j"]
			HorasProgram=relacion();
			#bajo los indicadores i j construimos la hora exacta
			hora=getHora(i)
			dias=j
			#data_flow=Horarios.objects.filter(Q(dia=dias)&Q(hora=hora.h)&Q(minutos=hora.m))
			#data["response"]=Horarios.objects.get(dia=dias,hora=hora.h,minutos=hora.m)
			#data["response"]="%s:%s"%(hora.h,hora.m)
			HorasProgram.horario=Horarios.objects.get(dia=dias,hora=hora.h,minutos=hora.m)
			if request.session["idAmb"]:
				HorasProgram.ambientes=Ambientes.objects.get(pk=request.session["idAmb"])
			else:
				data["response"]="No Selecciono el Ambiente"
				return HttpResponse(json.dumps(data),content_type="application/json")
			if request.session["idDoc"]:
				HorasProgram.docentes=Docente.objects.get(pk=request.session["idDoc"])
			else:
				data["response"]="No Selecciono el Docente"
				return HttpResponse(json.dumps(data),content_type="application/json")
			if request.session["idMat"]:
				HorasProgram.materia=Materia.objects.get(pk=request.session["idMat"])
			else:
				data["response"]="No selecciono la materia"
				return HttpResponse(json.dumps(data),content_type="application/json")
			if  request.session["idSem"]:
				HorasProgram.semestre=Semestres.objects.get(pk=request.session["idSem"])
			else:
				data["response"]="No Selecciono la materia"
				return HttpResponse(json.dumps(data),content_type="application/json")
			HorasProgram.fila=i
			HorasProgram.columna=j
			HorasProgram.save()
			data["response"]=True
			return HttpResponse(data["response"],content_type="application/html")
	return HttpResponse(json.dumps(data),content_type="application/json")
def borrarHorario(request,id):
	hora=relacion.objects.get(pk=int(id))
	hora.delete()
	data={}
	data["response"]=True
	return HttpResponse(data["response"],content_type="application/html")

def ListaDocentes(request):
	listaDocente=Docente.objects.all()
	listaMateria=Materia.objects.all()
	return render_to_response("lista.html",{"listaDoc":listaDocente,"listaMat":listaMateria},RequestContext(request))
def loadSem(request,id):
	request.session["idSem"]=id
	data={}
	data["response"]=request.session["idSem"]
	return HttpResponse(data["response"],content_type="application/html")
def reporteSemestre(request):
	semestre=Semestres.objects.all()
	return render_to_response("reporte.html",{"semestre":semestre},RequestContext(request))
def porSemestreReporte(request,id):
	sem=Semestres.objects.get(pk=id)
	if(request.session["code"]!=""):
		horario=relacion.objects.filter(semestre=sem,materia__sigla__contains=request.session["code"]).exclude(materia__sigla__contains="A.")
	else:
		horario=relacion.objects.filter(semestre=sem).exclude(materia__sigla__contains="A.")
	horas=[]
	for i in horario:
		horas.append({"idSem":id,"materia":"%s %s"%(i.materia,i.ambientes),"fila":"%s"%(i.fila),"columna":"%s"%(i.columna),"id":"%s"%(i.id)})
	return HttpResponse(json.dumps(horas),content_type="application/json")
def reporteDocente(request):
	#semestre=Semestres.objects.all()
	docente = Docente.objects.filter()
	list_doc = []
	for doc in docente:
		list_rel = relacion.objects.filter(docentes = doc)
		if(len(list_rel) > 0):
			list_doc.append(doc)
	return render_to_response("reporte2.html",{"docente" : list_doc},RequestContext(request))
def reporteAmbiente(request):
	ambientes=Ambientes.objects.all();
	return render_to_response("reporte3.html",{"ambientes":ambientes},RequestContext(request))	
def porDocenteReporte(request,id):
	doc=Docente.objects.get(Q(pk = id))
	if(request.session["code"]!=""):
		horario=relacion.objects.filter(docentes=doc,materia__sigla__contains=request.session["code"])
	else:
		horario=relacion.objects.filter(docentes=doc)
	horas=[]
	for i in horario:
		horas.append({"idSem":id,"materia":"%s %s"%(i.materia,i.ambientes),"fila":"%s"%(i.fila),"columna":"%s"%(i.columna),"id":"%s"%(i.id)})
	return HttpResponse(json.dumps(horas),content_type="application/json")
class Info:
	ins=""
	horas=""
	sem=""
class Lista:
	resultados=""
	dia=""
def imprimirPlanilla2(request):
	h=relacion.objects.filter(horario__dia=1).order_by("horario__hora","horario__minutos")
	return render_to_response("planilla2.html",{"r":h},RequestContext(request))
def imprimirPlanilla2(request):
	lista=[]
	dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
	for q in range(0,6):
		h=relacion.objects.filter(Q(horario__dia=q)&(Q(docentes__nombre__contains="Univ."))).order_by("horario__hora","horario__minutos")
		horas=list(h)
		c=0
		resultados=[]
		borrar=[]
		for i in range(0,len(horas)):
			if i<len(horas):
				c=0
				aux=horas[i].materia.sigla
				ins=horas[i]
				for j in range(0,len(horas)):
					if j<len(horas) and i!=j and aux==horas[j].materia.sigla:
						c+=1
						#horas.remove(horas[j])
						if j+1<len(horas) and horas[j].materia.sigla==horas[j+1].materia.sigla:
							horas.remove(horas[j+1])
							horas.remove(horas[j])
							c+=1
						else:
							horas.remove(horas[j])
				p=Info()
				c+=1
				obj=getHora(ins.fila+c)
				p.horas="%s:%s-%s:%s"%(ins.horario.hora,ins.horario.minutos,obj.h,obj.m)
				p.sem=ins.semestre.nombre.split(" ")[1]
				p.ins=ins
				resultados.append(p)
		s=Lista()
		s.resultados=resultados
		s.dia=dia[q]
		lista.append(s)
	return render_to_response("planilla.html",{"r":lista},RequestContext(request))
def imprimirPlanilla(request):
	lista=[]
	dia=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
	for q in range(0,6):
		h=relacion.objects.filter(Q(horario__dia=q)&(Q(docentes__nombre__contains="Ing.")|Q(docentes__nombre__contains="Lic.")|Q(docentes__nombre__contains="Por"))).order_by("horario__hora","horario__minutos")
		horas=list(h)
		c=0
		resultados=[]
		borrar=[]
		for i in range(0,len(horas)):
			if i<len(horas):
				c=0
				aux=horas[i].materia.sigla
				ins=horas[i]
				for j in range(0,len(horas)):
					if j<len(horas) and i!=j and aux==horas[j].materia.sigla and ins.semestre.nombre==horas[j].semestre.nombre:
						c+=1
						if j+1<len(horas) and horas[j].materia.sigla==horas[j+1].materia.sigla and horas[j].semestre.nombre==horas[j+1].semestre.nombre: 
							if j+2<len(horas) and horas[j].materia.sigla==horas[j+2].materia.sigla:
								horas.remove(horas[j+2])
								c+=1
							horas.remove(horas[j+1])
							horas.remove(horas[j])
							c+=1
						else:
							horas.remove(horas[j])
				p=Info()
				c+=1
				obj=getHora(ins.fila+c)
				if(ins.horario.minutos<10):
					Manother="0%s"%(ins.horario.minutos)
				else:
					Manother=ins.horario.minutos
				if(obj.m<10):
					Manother2="0%s"%(obj.m)
				else:
					Manother2=obj.m
				p.horas="%s:%s-%s:%s"%(ins.horario.hora,Manother,obj.h,Manother2)
				if(i+1<len(horas) and horas[i].horario.hora!=horas[i+1].horario.hora and horas[i+1].horario.hora==14):
					p.after=1;
				else:
					p.after=0;
				p.sem=ins.semestre.nombre.split(" ")[1]
				p.ins=ins
				resultados.append(p)
		s=Lista()
		s.resultados=resultados
		s.dia=dia[q]
		lista.append(s)
	return render_to_response("planilla.html",{"r":lista},RequestContext(request))

def materiasjson(request):
	materia=Materia.objects.all();
	listamat=[]
	for mat  in materia:
		listamat.append({"name":"%s %s"%(mat.sigla,mat.nombre),"id":mat.id});
	return HttpResponse(json.dumps(listamat),content_type="application/json")

def updatemateria(request):
	materiaid=request.POST["idMat"]
	docenteid=request.POST["idDoc"]
	mat=Materia.objects.get(pk=materiaid);
	doc=Docente.objects.get(pk=docenteid)
	doc.materia.add(mat)
	doc.save();
	return HttpResponse(json.dumps({"succes":True,"id":docenteid}),content_type="application/json")
def deletemateria(request):
	materiaid=request.POST["idMat"]
	docenteid=request.POST["idDoc"]
	#pdb.set_trace()
	mat=Materia.objects.get(pk=materiaid)
	doc=Docente.objects.get(pk=docenteid)
	doc.materia.remove(mat)
	lista=relacion.objects.filter(docentes=doc,materia=mat)
	for i in lista:
		i.delete()
	#return HttpResponseRedirect("/lista/");
	return HttpResponse(json.dumps({"succes":True,"id":docenteid}),content_type="application/json")