// this document regulates the persistent elements (navbars, etc)...
// that may need to appear in several pages

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

class FooterBar extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
		<ul class="navbar-ul">
			<li class="navbar-item">E-Mail: <a href="mailto:cattette@proton.me">cattette@proton.me</a></li>
			<li class="navbar-item">Hosted by: <a href="https://web1.0hosting.net/">Web1.0</a></li>				
			<li class="navbar-item"><a href="https://github.com/Cattette/cattette-website">Git Repo</a></li>				
		</ul>
    `;
  }
}

customElements.define('my-navbar', MyNavbar);
customElements.define('my-footer', FooterBar);
