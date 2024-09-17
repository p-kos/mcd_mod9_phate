import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>
</head>
<body>

<h1>PHATE</h1>
<h2>Potential of Heat-diffusion for Affinity-based Transition Embedding</h2>
<h3>Jhaazel Colque - Nicole Condori - Marco Zárate<h3>
<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>  
  <img src="https://scontent.fcbb2-1.fna.fbcdn.net/v/t1.6435-9/141975643_4034939026556918_5618410493593755665_n.jpg?stp=dst-jpg_s1080x2048&_nc_cat=106&ccb=1-7&_nc_sid=13d280&_nc_ohc=PA2W2Q-Efg0Q7kNvgGeAPEZ&_nc_ht=scontent.fcbb2-1.fna&oh=00_AYBF6ZnFiiUmQBwK6sY9rKkXzaXm2ldXcT4l7aijUjTJug&oe=67105BC2" style="width:100%">
  <div class="text">Jhazeel Colque - Nicole Condori - Marco Zárate</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>  
  <ul>
    <li>Algoritmo para reducir la dimensionalidad</li>
    <li>Author: Krishnaswamy lab</li>
    <li>Diseñado para capturar estructuras no lineales complejas</li>
    <li>Ej: Imágenes, datos genómicos</li>
  </ul>
  
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <h3>Características</h3>
  <ul>
    <li>Captura de estructuras no lineales</li>
    <li>Preserva estructuras globales y locales</li>
    <li>Visualización en baja dimensionalidad</li>
  </ul>
  
</div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
</script>

</body>
</html> 
    """,
    height=600,
)