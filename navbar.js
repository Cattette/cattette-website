class MyNavbar extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
		<nav class="navbar">
			<ul class="navbar-ul">
			  <li class="navbar-item"><a href="index.html">Home</a></li>
			  <li class="navbar-item"><a href="about.html">About</a></li>
			  <li class="navbar-item"><a href="maps.html">Maps</a></li>
			  <li class="navbar-item"><a href="projects.html">Other art</a></li>
			  <li class="navbar-item"><a href="misc.html">Misc</a></li>
			</ul>
		</nav>
    `;
  }
}
customElements.define('my-navbar', MyNavbar);
