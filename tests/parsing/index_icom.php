<!DOCTYPE HTML>
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=Edge" >
<title>Oferta de Cursos</title>
<script type="text/javascript">
function verifyTid() {
	tid = document.getElementById("tid");
	tid.value = tid.value.replace(/^\s+|\s+$/g, '');
	if(tid.value.length == 0) {
	  alert("Escriba el numero de transaccion.");
	}
	return true;
	switch(tid.value[0]) {
		case '7':
			if(tid.value.length != 20) {
			  alert("Este numero de transaccion es invalido. [ERR007]");
			  return false;
			}
			break;
		case '9':
			if(tid.value.length != 26) {
			  alert("Este numero de transaccion es invalido. [ERR009]");
			  return false;
			}
			break;
		default:
			alert("Este numero de transaccion es invalido. [INVALID]");
			return false;
			break;
	}
	return true;
}
</script>
<link rel='stylesheet' type='text/css' href='/registrar/css/contact.css'>
<link rel="shortcut icon" href="/registrar/favicon.ico" type="image/x-icon">

<!-- ====================Fonts===================== -->
 <style>
 @font-face {
  font-family: 'Spinnaker';
  font-style: normal;
  font-weight: 400;
  src: local('Spinnaker'), local('Spinnaker-Regular'), url(//themes.googleusercontent.com/static/fonts/spinnaker/v5/WxzDAY6mC9v3znSJEtCoWz8E0i7KZn-EPnyo3HZu7kw.woff) format('woff');
}
@font-face {
  font-family: 'Cabin';
  font-style: normal;
  font-weight: 400;
  src: local('Cabin Regular'), local('Cabin-Regular'), url(//themes.googleusercontent.com/static/fonts/cabin/v4/JEgmtEDzc-IH8jBshQXrYA.woff) format('woff');
}
@font-face {
  font-family: 'PT Sans Caption';
  font-style: normal;
  font-weight: 400;
  src: local('PT Sans Caption'), local('PTSans-Caption'), url(//themes.googleusercontent.com/static/fonts/ptsanscaption/v5/OXYTDOzBcXU8MTNBvBHeSQRW432DtwGNER78eOJ0i0s.woff) format('woff');
}
</style>
<!-- ===================End Fonts================== -->

<!--[if IE]>
<link rel='stylesheet' type='text/css' href='/portada/css/all_ie.css' /><![endif]-->

<!-- =================CSS================== -->
<link rel='stylesheet' type='text/css' href='/registrar/css/portada.css'>
<link rel='stylesheet' type='text/css' href='/registrar/css/registrar.css'>
<link rel='stylesheet' type='text/css' href='/registrar/css/page_base.css'>
<link href="/registrar/menu_assets/styles.css" rel="stylesheet" type="text/css">
<link href="/registrar/css/usu.css" rel="stylesheet" type="text/css" media="screen">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8/jquery.min.js" type="text/javascript"></script>
<link rel='stylesheet' type='text/css' href='/registrar/css/print.css' media="print">

<!-- =================END CSS================== -->

<meta name="google-site-verification" content="#" >
<meta name="keywords" lang="ES" content="Registraduria, UPR, Mayaguez, Universidad, Puerto, Rico, UPRM, Briseida, Melendez, Oficina, Registrador, Servicios, Linea, Transcripcion, Creditos, Certificacion, Estudiante, Regular"
<meta name="description" lang="ES" content="En nuestro portal encontraras todos los servicios que ofrece la Oficina de Registraduria.">
<meta name="author" lang="ES" content="Universidad de Puerto Rico: Recinto Universitario de Mayaguez">
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
     
<!--[if !IE 7]><style type="text/css">#idx_page_container {display:table;height:100%}</style><![endif]-->
</head>


<!-- Start: Verifica si es un celular y lo reenvia a su version correspondiente -->
<div>
  <script type="text/javascript" >

if(window.location.href.match(/mobile=false/i)) {
         today = new Date();
	 expires_date = new Date( today.getTime() + 86400000);
	 document.cookie = "iphone_redirect=false;expire=" + expires_date.toGMTString();
  }
  if((navigator.userAgent.match(/iphone|ipod|android|blackberry/i)) || (navigator.userAgent.match(/iPod/i))) {
       var pathname = window.location.pathname.substring(11);
	 if (document.cookie.indexOf("iphone_redirect=false") == -1) window.location = "/registrar/mobile/" + pathname;
}
</script>

<script type="text/javascript">
   var ua = navigator.userAgent;
   var url = "/registrar/mobile/" + pathname;
   if (ua.indexOf("BlackBerry") >= 0)
   {
      if (ua.indexOf("WebKit") >= 0)
      {
         window.location = url;
      }
   }
</script>
</div>
<!-- End: Verifica si es un celular y lo reenvia a su version correspondiente -->
<!------------------------------Head-------------------------------->

<body><img src='../media/porticobg.gif' alt='portico' class='portada_portico'><div id='idx_page'><a id='skipnav' href="#main">Skip Navigation</a><div id='idx_page_container'><div id="idx_page_mnu"><div id='idx_page_rum'><img src='../media/logo_rum.png' class="logotop" width='120' height='120' alt='RUM' title='University logo' onclick='window.location.href = "http://www.uprm.edu/portada/";'></div><div id="idx_page_rum_mnu"><script type="text/javascript" name="orgmnu" src="../css/uprm_menusp.js"></script><a id="atglance_link" href="#" onclick="smn_toogle(); return false;" title="mapa del sitio">m&aacute;s...</a><div id='mnu_social'></div></div></div><!-- end idx_page_mnu --><div id='uprm_full_mnu_ct' style='display: none;'><div id='uprm_full_mnu_ctx'><div class='col'><ul><li class='title'><a href='http://admisiones.uprm.edu/' title='Admisiones'>Admisiones</a></li><li><a href='http://admisiones.uprm.edu/stdnew.html' title='Estudiantes de Nuevo Ingreso'>Estudiantes de nuevo ingreso</a></li><li><a href='http://www.uprm.edu/netpricecalculator' title='Estima el costo de tus estudios'>Estima el costo de tus estudios</a></li><li><a href='http://grad.uprm.edu/' title='Escuela Graduada'>Estudios graduados</a></li></ul><ul><li class='title'><a href='http://www.uprm.edu/library/' title='Biblioteca General'>Biblioteca General</a></li></ul><ul><li class='title'><a href='https://home.uprm.edu/' title='Mi Portal Colegial'>Mi UPRM</a></li></ul><ul><li class='title'><a href='http://moodle.uprm.edu/' title='e-Courses by Moodle'>eCourses</a></li></ul></div><div class='col'><ul><li class='title'><a href='http://research.uprm.edu/' title='Investigaci&oacute;n'>Investigaci&oacute;n</a></li><li><a href='http://cid.uprm.edu/' title='Centro de Investigaci&oacute;n y Desarrollo'>Centro de Investigaci&oacute;n y Desarrollo</a></li><li><a href='http://eea.uprm.edu/' title='Estaci&oacute;n Experimental Agr&iacute;cola'>Estaci&oacute;n Experimental Agr&iacute;cola</a></li></ul><ul><li class='title'><a href='http://academico.uprm.edu/' title='Acad&eacute;micos'>Acad&eacute;micos</a></li><li><a href='http://www.uprm.edu/matricula/' title='Proceso de Matr&iacute;cula'>Matr&iacute;cula</a></li><li><a href='http://aeconomica.uprm.edu/' title='Asistencia Econ&oacute;mica'>Asistencia econ&oacute;mica</a></li><li><a href='http://www.uprm.edu/registrar/' title='Registradur&iacute;a'>Registradur&iacute;a</a></li><li><a href='http://www.uprm.edu/registrar/solicitudes/index.php' title='Solicitudes, Transcripci&oacute;n de cr&eacute;ditos, Certificaci&oacute;nes...'>Solicitud de documentos</a></li></ul></div><div class='col'><ul><li class='title'><a href='http://administracion.uprm.edu/' title='Administraci&oacute;n'>Administraci&oacute;n</a></li><li><a href='http://www.uprm.edu/decadmi/' title='Decanato de Administraci&oacute;n'>Decanato de Administraci&oacute;n</a></li><li><a href='http://www.uprm.edu/rectoria/' title='Rectoria'>Rectoria</a></li><li><a href='http://www.uprm.edu/decadmi/finanzas/payments/index.php' title='Recaudaciones, Pago en l&iacute;nea...'>Recaudaciones</a></li></ul></div><div class='col'><ul><li class='title'><a href='http://estudiantes.uprm.edu/' title='Estudiantes'>Estudiantes</a></li><li><a href='http://academico.uprm.edu/srtk.html' title='Derecho del estudiante a saber'>Derecho del estudiante a saber</a></li><li><a href='http://www.uprm.edu/orientacion/' title='Orientaci&oacute;n'>Consejer&iacute;a y psicolog&iacute;a</a></li><li><a href='http://procuraduria.uprm.edu/' title='Procuradur&iacute;a Estudiantil'>Procuradur&iacute;a estudiantil</a></li><li><a href='http://www.uprm.edu/medical/SM/' title='Servicios M&eacute;dicos'>Servicios m&eacute;dicos</a></li></ul><ul><li class='title'><a href='http://www.uprm.edu/about/' title='Conoce la universidad'>Conoce la universidad</a></li><li><a href='http://www.uprm.edu/travel/' title='De visita en el recinto, como llegar, mapa del recinto, informaci&oacute;n para viajeros'>Visitantes</a></li></ul></div></div><img src='../media/closebox.png' alt='closebox' class='closebox' onclick='smn_toogle(); return false;'></div><div id='idx_page_body'></div><!-- end idx_page_body --></div><!-- end idx_page_container --><!------------------------------Top-------------------------------->


<div id="Wrap"><!---------------------------------------Start Content of Register------------------------------------------------->

<div id="Header">

</div><!---------------------------------------End Header----------------------------->


<div id="Menu">
<center>
<div class='cssmenu'>
<ul>
   <li><a href='/registrar/index.php'><span>Inicio</span></a></li>
   <li><a href='/registrar/solicitudes.php'><span>Solicitudes y Costos</span></a></li>
    <li><a><span>Servicios en L&#237;nea</span></a>
      <ul>
         <li><a href='/registrar/services/pago.php'><span>Pago en L&#237;nea</span></a></li>
         <li><a href='/registrar/services/form.php?new'><span>Completar Solicitud en L&#237;nea</span></a></li>
         <li><a href='/registrar/services/status.php'><span>Estatus de Solicitud</span></a></li>
      </ul>
   </li>
   <li><a><span>Estudiantes</span></a>
      <ul>

            <li><a href='/registrar/matricula.php'><span>Matr&#237;cula</span></a></li>
            <li><a href='/registrar/readmision.php'><span>Readmisi&#243;n & Traslado</span></a></li>
            <li><a href='/registrar/graduacion.php'><span>Graduaci&#243;n</span></a></li>
            <li><a href='/registrar/progreso.php'><span>Progreso Acad&#233;mico</span></a></li>
            <li><a href='/registrar/veteranos.php'><span>Veteranos</span></a></li>
            <li><a href='/registrar/ley203.php'><span>Ley 203</span></a></li>
            <li><a href='/registrar/sections/'><span>Oferta de Cursos</span></a></li>
      </ul>
   </li>
   <li><a href='/registrar/padres.php'><span>Padres</span></a></li>

   <li><a><span>Leyes</span></a>
      <ul>
            <li><a href='/registrar/ferpa.php'><span>Ley Ferpa</span></a></li>
      </ul>
   </li>
   <li><a><span>Nuestra Oficina</span></a>
      <ul>
         <li><a href='/registrar/contact.php'><span>Cont&#225;ctanos</span></a></li>
         <li><a href='/registrar/directorio.php'><span>Directorio</span></a></li>
         <li><a href='/registrar/evaluacion/'><span>Evalua Nuestros Servicios</span></a></li>
      </ul>
   </li>
   <li><a href='/registrar/faq.php'><span>Preguntas Frecuentes</span></a></li>
   <li><a href='/registrar/glossary2.php'><span>Glosario</span></a></li>
   <li><a href='/registrar/documentos.php'><span>Documentos</span></a></li>
</ul>
</div><!-- cssmenu -->
</center>
</div><!-- ===============================End Menu=============================== -->
<!------------------------------Menu-------------------------------->

<div id="Content" style="width:90%;">

<p>

	<div id='searchpane'><div class='header'><h2>Search sections</h2></div><div class='body'><form name='frm1' method='GET' action='index.php' onsubmit='return submitForm(this);'><h3>Enter Course (eg ECON or ECON3021 or ECON4)</h3><input type='text' size='20' value='icom' name='v1'><br><br><h3><input type='checkbox' class='checkbox' value='1' name='op2'> By Professor</h3>  <br><input type='text' size='30' value='' name='v2'><br><h3>Term</h3><select name='term'><option value='3-2024'>Spring Semester-2024</option>
<option value='2-2024' selected>Fall Semester-2024</option>
<option value='1-2024'>First Summer, 4 weeks-2024</option>
<option value='5-2024'>Extended Summer, 6 weeks-2024</option>
<option value='4-2024'>Second Summer, 4 weeks-2024</option>
</select><br><br><input type='hidden' name='a' value='s'><input type='submit' name='cmd1' class='button' value='Search'><br><br></form></div></div><script type='text/javascript'>
function submitForm(f){
if(f.v1.lenght < 4){
alert('Invalid course value');
f.v1.focus();
return false;
}
var v = document.getElementById('sections_wait');
v.style.display = 'block';
v = document.getElementById('results_table');
if(v) v.style.display = 'none';
return true;}
</script><div id='sections_wait' style='display: none;'><img src='ui_loading01.gif' width='32' height='32' alt='Progress bar'></div>







<table border='0' class='section_results' id='results_table'>
<tr><th></th><th>Course</th><th>Credits</th><th></th><th>Meetings</th><th>Professor(s)</th></tr>
<tr><td class='odd'>1</td><td class='odd'>SOFTWARE ENGINEERING<br><b>ICOM4009-080</b></td><td class='odd'>3</td><td class='odd'>LowerDivision</td><td class='odd'>2:30 pm - 3:20 pm &nbsp;LWV &nbsp;&nbsp;S 113<br></td><td class='odd'>Marko Schutz<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4035, Co-Requisites: <br></td></tr>
<tr><td class='even'>2</td><td class='even'>ADVANCED PROGRAMMING<br><b>ICOM4015-020L</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>8:30 am - 10:20 am &nbsp;V &nbsp;&nbsp;S 114a<br></td><td class='even'>Misael Mercado Hernandez<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='odd'>3</td><td class='odd'>ADVANCED PROGRAMMING<br><b>ICOM4015-021L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>8:30 am - 10:20 am &nbsp;V &nbsp;&nbsp;S 121<br></td><td class='odd'>Jann Garcia Pagan<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='even'>4</td><td class='even'>ADVANCED PROGRAMMING<br><b>ICOM4015-040L</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>10:30 am - 12:20 pm &nbsp;V &nbsp;&nbsp;S 114a<br></td><td class='even'>JOMARD         CONCEPCION      ROMAN<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='odd'>5</td><td class='odd'>ADVANCED PROGRAMMING<br><b>ICOM4015-041L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>10:30 am - 12:20 pm &nbsp;V &nbsp;&nbsp;S 121<br></td><td class='odd'>Jose Ortiz Baez<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='even'>6</td><td class='even'>ADVANCED PROGRAMMING<br><b>ICOM4015-060L</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>12:30 pm - 2:20 pm &nbsp;V &nbsp;&nbsp;S 114a<br></td><td class='even'>Jose Cordero Velez<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='odd'>7</td><td class='odd'>ADVANCED PROGRAMMING<br><b>ICOM4015-061L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>12:30 pm - 2:20 pm &nbsp;V &nbsp;&nbsp;S 121<br></td><td class='odd'>ROBDIEL A MELENDEZ ROSADO<br>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='even'>8</td><td class='even'>ADVANCED PROGRAMMING<br><b>ICOM4015-120</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>6:00 pm - 7:15 pm &nbsp;LW &nbsp;&nbsp;<br></td><td class='even'>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='odd'>9</td><td class='odd'>ADVANCED PROGRAMMING<br><b>ICOM4015-120E</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>6:00 pm - 7:15 pm &nbsp;LW &nbsp;&nbsp;<br></td><td class='odd'>Gretchen Bonilla Caraballo<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> INGE3016, Co-Requisites: <br></td></tr>
<tr><td class='even'>10</td><td class='even'>DATA STRUCTURES<br><b>ICOM4035-030L</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>9:30 am - 11:20 am &nbsp;L &nbsp;&nbsp;S 114a<br></td><td class='even'>JOSE           QUINONES        VELEZ<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='odd'>11</td><td class='odd'>DATA STRUCTURES<br><b>ICOM4035-031L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>9:30 am - 11:20 am &nbsp;L &nbsp;&nbsp;S 121<br></td><td class='odd'>Jean Montes Santiago<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='even'>12</td><td class='even'>DATA STRUCTURES<br><b>ICOM4035-036</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>9:00 am - 10:15 am &nbsp;MJ &nbsp;&nbsp;S 113<br></td><td class='even'>Arturo Ponce Roman<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='odd'>13</td><td class='odd'>DATA STRUCTURES<br><b>ICOM4035-050L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>11:30 am - 1:20 pm &nbsp;L &nbsp;&nbsp;S 114a<br></td><td class='odd'>FABIOLA ROZAS FLORES<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='even'>14</td><td class='even'>DATA STRUCTURES<br><b>ICOM4035-051L</b></td><td class='even'>4</td><td class='even'>LowerDivision</td><td class='even'>11:30 am - 1:20 pm &nbsp;L &nbsp;&nbsp;S 121<br></td><td class='even'>OSCAR CONDORI OCHOA<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='odd'>15</td><td class='odd'>DATA STRUCTURES<br><b>ICOM4035-070L</b></td><td class='odd'>4</td><td class='odd'>LowerDivision</td><td class='odd'>1:30 pm - 3:20 pm &nbsp;L &nbsp;&nbsp;S 114a<br></td><td class='odd'>FABIOLA ROZAS FLORES<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4015 Y MATE3031 Y ICOM4075, Co-Requisites: <br></td></tr>
<tr><td class='even'>16</td><td class='even'>STRUCTURE AND PROPERTIES OF PROGRAMMING LANGUAGES<br><b>ICOM4036-066</b></td><td class='even'>3</td><td class='even'>LowerDivision</td><td class='even'>12:30 pm - 1:45 pm &nbsp;MJ &nbsp;&nbsp;S 113<br></td><td class='even'>Wilson Rivera Gallego<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4035, Co-Requisites: <br></td></tr>
<tr><td class='odd'>17</td><td class='odd'>ALGORITHM DESIGN AND ANALYSIS<br><b>ICOM4038-016</b></td><td class='odd'>3</td><td class='odd'>LowerDivision</td><td class='odd'>7:30 am - 8:45 am &nbsp;MJ &nbsp;&nbsp;S 113<br></td><td class='odd'>Wilfredo Lugo Beauchamp<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4035, Co-Requisites: <br></td></tr>
<tr><td class='even'>18</td><td class='even'>FOUNDATIONS OF COMPUTING<br><b>ICOM4075-030</b></td><td class='even'>3</td><td class='even'>LowerDivision</td><td class='even'>9:30 am - 10:20 am &nbsp;LWV &nbsp;&nbsp;S 113<br></td><td class='even'>Kejie Lu<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: INGE3016<br></td></tr>
<tr><td class='odd'>19</td><td class='odd'>FOUNDATIONS OF COMPUTING<br><b>ICOM4075-086</b></td><td class='odd'>3</td><td class='odd'>LowerDivision</td><td class='odd'>2:00 pm - 3:15 pm &nbsp;MJ &nbsp;&nbsp;<br></td><td class='odd'>Kejie Lu<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: INGE3016<br></td></tr>
<tr><td class='even'>20</td><td class='even'>COMPUTER ARQUITECTURE AND ORGANIZATION<br><b>ICOM4215-086H</b></td><td class='even'>3</td><td class='even'>LowerDivision</td><td class='even'>2:00 pm - 3:15 pm &nbsp;MJ &nbsp;&nbsp;S 228<br></td><td class='even'>Nestor Rodriguez<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> INEL4206, Co-Requisites: <br></td></tr>
<tr><td class='odd'>21</td><td class='odd'>NETWORKING AND ROUTING FUNDAMENTALS<br><b>ICOM4308-066</b></td><td class='odd'>3</td><td class='odd'>LowerDivision</td><td class='odd'>12:30 pm - 1:45 pm &nbsp;MJ &nbsp;&nbsp;S 222<br></td><td class='odd'>Isidoro Couvertier Reyes<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> MATE3063 O DIR, Co-Requisites: <br></td></tr>
<tr><td class='even'>22</td><td class='even'>ENGINEERING PRACTICE COOP<br><b>ICOM4995-001P</b></td><td class='even'>3</td><td class='even'>LowerDivision</td><td class='even'></td><td class='even'>Ramon Vasquez Espinosa<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>23</td><td class='odd'>UNDERGRADUATE RESEARCH<br><b>ICOM4998-001R</b></td><td class='odd'>3</td><td class='odd'>LowerDivision</td><td class='odd'></td><td class='odd'>Nayda Santiago Santiago<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> DIR Y (4TO O 5TO), Co-Requisites: <br></td></tr>
<tr><td class='even'>24</td><td class='even'>OPERATING SYSTEMS PROGRAMMING<br><b>ICOM5007-070L</b></td><td class='even'>4</td><td class='even'>UpperDivision</td><td class='even'>1:30 pm - 4:20 pm &nbsp;W &nbsp;&nbsp;S 114a<br></td><td class='even'>Derel Rivera Guzman<br>Juan Medina Lee<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> (ICOM4035 Y INEL4206) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>25</td><td class='odd'>OPERATING SYSTEMS PROGRAMMING<br><b>ICOM5007-071L</b></td><td class='odd'>4</td><td class='odd'>UpperDivision</td><td class='odd'>1:30 pm - 4:20 pm &nbsp;W &nbsp;&nbsp;S 121<br></td><td class='odd'>OMAR TORRES BOLANO<br>Juan Medina Lee<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> (ICOM4035 Y INEL4206) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='even'>26</td><td class='even'>OPERATING SYSTEMS PROGRAMMING<br><b>ICOM5007-096</b></td><td class='even'>4</td><td class='even'>UpperDivision</td><td class='even'>3:30 pm - 4:45 pm &nbsp;MJ &nbsp;&nbsp;S 113<br></td><td class='even'>Juan Medina Lee<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> (ICOM4035 Y INEL4206) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>27</td><td class='odd'>OPERATING SYSTEMS PROGRAMMING<br><b>ICOM5007-100L</b></td><td class='odd'>4</td><td class='odd'>UpperDivision</td><td class='odd'>4:30 pm - 7:20 pm &nbsp;W &nbsp;&nbsp;S 114a<br></td><td class='odd'>Juan Medina Lee<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> (ICOM4035 Y INEL4206) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='even'>28</td><td class='even'>OPERATING SYSTEMS PROGRAMMING<br><b>ICOM5007-101L</b></td><td class='even'>4</td><td class='even'>UpperDivision</td><td class='even'>4:30 pm - 7:20 pm &nbsp;W &nbsp;&nbsp;S 121<br></td><td class='even'>OMAR TORRES BOLANO<br>Juan Medina Lee<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> (ICOM4035 Y INEL4206) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>29</td><td class='odd'>DATABASE SYSTEMS<br><b>ICOM5016-116</b></td><td class='odd'>3</td><td class='odd'>UpperDivision</td><td class='odd'>5:00 pm - 6:15 pm &nbsp;MJ &nbsp;&nbsp;S 113<br></td><td class='odd'>Manuel Rodriguez Martinez<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM4035 O DIR, Co-Requisites: <br></td></tr>
<tr><td class='even'>30</td><td class='even'>CRYPTOGRAPHY AND NETWORK SECURITY<br><b>ICOM5018-050</b></td><td class='even'>3</td><td class='even'>UpperDivision</td><td class='even'>11:30 am - 12:20 pm &nbsp;LWV &nbsp;&nbsp;S 113<br></td><td class='even'>Venkataramani  Kumar<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ICOM5007 O DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>31</td><td class='odd'>COMPUTER ENGINEERING PROJECT DESIGN<br><b>ICOM5047-016</b></td><td class='odd'>3</td><td class='odd'>UpperDivision</td><td class='odd'>7:30 am - 10:20 am &nbsp;M &nbsp;&nbsp;S 122<br>8:30 am - 10:20 am &nbsp;J &nbsp;&nbsp;S 122<br></td><td class='odd'>Isidoro Couvertier Reyes<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> ((ICOM4009 O ICOM5016) Y (ICOM4217 O INEL5206 O INEL5265) Y ICOM4215 Y ICOM5007 Y INEL4301 Y INEL4207) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='even'>32</td><td class='even'>COMPUTER ENGINEERING PROJECT DESIGN<br><b>ICOM5047-017</b></td><td class='even'>3</td><td class='even'>UpperDivision</td><td class='even'>7:30 am - 10:20 am &nbsp;M &nbsp;&nbsp;S 123<br>8:30 am - 10:20 am &nbsp;J &nbsp;&nbsp;S 123<br></td><td class='even'>Nayda Santiago Santiago<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> ((ICOM4009 O ICOM5016) Y (ICOM4217 O INEL5206 O INEL5265) Y ICOM4215 Y ICOM5007 Y INEL4301 Y INEL4207) O DIR, Co-Requisites: <br></td></tr>
<tr><td class='odd'>33</td><td class='odd'>ARTIFICIAL NEURAL NETWORKS<br><b>ICOM6015-001D</b></td><td class='odd'>3</td><td class='odd'>Graduate</td><td class='odd'></td><td class='odd'>Jose Vega Riveros<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='even'>34</td><td class='even'>HUMAN-COMPUTER INTERACTION<br><b>ICOM6095-001D</b></td><td class='even'>3</td><td class='even'>Graduate</td><td class='even'></td><td class='even'>Nestor Rodriguez<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='odd'>35</td><td class='odd'>INDEPENDENT STUDIES IN COMPUTER ENGINEERING<br><b>ICOM6995-001#</b></td><td class='odd'>0</td><td class='odd'>Graduate</td><td class='odd'></td><td class='odd'>Nayda Santiago Santiago<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='even'>36</td><td class='even'>MASTERS PROJECT<br><b>ICOM6998-001#</b></td><td class='even'>0</td><td class='even'>Graduate</td><td class='even'></td><td class='even'>Eduardo Ortiz Rivera<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='odd'>37</td><td class='odd'>MASTERS THESIS<br><b>ICOM6999-001#</b></td><td class='odd'>3</td><td class='odd'>Graduate</td><td class='odd'></td><td class='odd'>Jose Vega Riveros<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='even'>38</td><td class='even'>MASTERS THESIS<br><b>ICOM6999-002#</b></td><td class='even'>3</td><td class='even'>Graduate</td><td class='even'></td><td class='even'>Manuel Rodriguez Martinez<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='odd'>39</td><td class='odd'>MASTERS THESIS<br><b>ICOM6999-003#</b></td><td class='odd'>0</td><td class='odd'>Graduate</td><td class='odd'></td><td class='odd'>Emmanuel Arzuaga Cruz<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='even'>40</td><td class='even'>MASTERS THESIS<br><b>ICOM6999-004#</b></td><td class='even'>0</td><td class='even'>Graduate</td><td class='even'></td><td class='even'>Manuel Jimenez Cedeno<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='odd'>41</td><td class='odd'>MASTERS THESIS<br><b>ICOM6999-005#</b></td><td class='odd'>0</td><td class='odd'>Graduate</td><td class='odd'></td><td class='odd'>Nayda Santiago Santiago<br></td></tr>
<tr><td class='odd extrainfo'></td><td class='odd extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr>
<tr><td class='even'>42</td><td class='even'>MASTERS THESIS<br><b>ICOM6999-006#</b></td><td class='even'>0</td><td class='even'>Graduate</td><td class='even'></td><td class='even'>Heidy Sierra Gil<br></td></tr>
<tr><td class='even extrainfo'></td><td class='even extrainfo' colspan='5'><b>Enrollment Requisites:</b> , Co-Requisites: <br></td></tr></table>








</p>

</div><!--------------------------------------End Content---------------------->

<div style="clear:both;"></div>
</div><!-----End Wrap---><!--------------------------End Content of Register------------------------------------------------------>

<div id='idx_page_footer'>
<div id='idx_page_footer_body'>
	<div id='idx_page_address'>
		<b>Universidad de Puerto Rico</b><br>
		<b>Recinto Universitario de Mayag&uuml;ez</b><br>
		<b style='font-size: .8em;'>Oficina de Registradur&#237;a</b>
		<br>CALL BOX 9000<br>Mayag&uuml;ez PR 00681-9000
	</div>
	<ul>
		<li><a href='http://www.uprm.edu/about' title='conoce la universidad'>conoce la universidad</a></li>
		<li><a href='http://academico.uprm.edu/srtk.html' title='derecho a saber'>derecho a saber</a></li>
		<li><a href='http://www.uprm.edu/contact' title='cont&aacute;ctenos'>cont&aacute;ctenos</a></li>
	</ul>
	<ul>
		<li><a href='http://centenario.uprm.edu' title='cien a&ntilde;os de historia...'>cien a&ntilde;os...</a></li>
		<li><a href='http://www.uprm.edu/prensa' title='oficina de prensa'>oficina de prensa</a></li>
		<li><a href='http://www.uprm.edu/welcomecenter' title='visitantes'>visitantes</a></li>
	</ul>
	<ul>
		<li><a href='http://www.uprm.edu/portada/emergency.php' title='emergencias'>emergencias</a></li>
		<li><a href='http://www.uprm.edu/politicas' title='pol&iacute;ticas institucionales'>pol&iacute;ticas institucionales</a></li>
		<li><a href='http://www.uprm.edu/wdt/pol01.html' title='pol&iacute;tica de privacidad'>pol&iacute;tica de privacidad</a></li>
	</ul>
	<ul>
		<li><a href="/registrar/sitemap.php" title="mapa del sitio">mapa del sitio</a></li>
		<li><a href="https://www.facebook.com/registraduriauprm" title="Fan Page de Registraduría" target="_blank">facebook: registraduría</a></li>
		<!--<li><a href="mobile/index.php" title="versi&#243;n ligera">versi&#243;n ligera&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</a></li>-->
	</ul>
	<div class='footer-contact'>
		<b>Cont&#225;ctanos:</b>
		<br><b>Tel:</b> (787) 832-4040&nbsp;&nbsp;&nbsp;&nbsp;Ext. 3813
		<br><b>Fax:</b> (787) 832-7828
		<br><b>Correo-e:</b> <a href="mailto:registro@uprm.edu">registro@uprm.edu</a>
	</div>
</div><!-- idx_page_footer_body -->
</div><!-- idx_page_footer -->

<!-- Start of StatCounter Code for Default Guide -->
<script type="text/javascript">
var sc_project=8998520;
var sc_invisible=1;
var sc_security="d7b6dd41";
var scJsHost = (("https:" == document.location.protocol) ?
"https://secure." : "http://www.");
document.write("<sc"+"ript type='text/javascript' src='" +
scJsHost+
"statcounter.com/counter/counter.js'></"+"script>");
</script>
<noscript><div class="statcounter"><a title="shopify
analytics ecommerce tracking"
href="http://statcounter.com/shopify/" target="_blank"><img
class="statcounter"
src="http://c.statcounter.com/8998520/0/d7b6dd41/1/"
alt="shopify analytics ecommerce
tracking"></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->





</body>
</html>

</body>
</html>
