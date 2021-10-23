/**
* @namespace
*/
D2LMathML = {

	IsLatex: false,

	IsMathJaxRequested: false,

	ReadyState: null,

	/**
	* @private
	*/
	m_message: '',

	/**
	* @private
	*/
	m_afterPartialHandler: null,

	/**
	* @private
	*/
	m_hasAfterPartialEvent: function() {
		return (window.D2L && window.D2L.LP && window.D2L.LP.Web
			&& window.D2L.LP.Web.UI && window.D2L.LP.Web.UI.Html
			&& window.D2L.LP.Web.UI.Html.PartialRendering
			&& window.D2L.LP.Web.UI.Html.PartialRendering.OnAfter);
	},

	DesktopInit: function (mathMLUrl, latexUrl, scalingFactor, renderLatex) {

		var isMathJaxLoaded = function () {
			if (document.head.querySelector('#mathJax')) {
				return true;
			}
			return false;
		};

		var isMathJaxRequired = function () {
			if (this.IsLatex || this.IsMathJaxRequested || document.querySelector('math') || (renderLatex && document.body && document.body.innerText && /\$\$|\\\(|\\\[|\\begin{|\\ref{/.test(document.body.innerText)) ) {
				return true;
			}
			return false;
		}.bind(this);

		var loadMathJax = function () {

			if (D2LMathML.ReadyState) {
				return;
			}

			D2LMathML.ReadyState = 'loading';

			var mathJaxConfig = {
				delayStartupUntil: "onload",
				showProcessingMessages: false,
				messageStyle: "none",
				menuSettings: {
					context: "MathJax",
					zoom: "None"
				},
				NativeMML: {
					showMathMenuMSIE: false,
					scale: scalingFactor + 10
				},
				"HTML-CSS": {
					linebreaks: {
						automatic: true,
						width: "container"
					},
					imageFont: null,
					scale: scalingFactor
				},
				styles: {
					".MathJax .merror": {
						"background-color": "#fff !important",
						color: "#494c4e !important",
						border: "1px solid #cd2026 !important"
					}
				}
			};

			if (renderLatex) {
				mathJaxConfig.tex2jax = {
					displayMath: [['$$', '$$'], ['\\[', '\\]']],
					inlineMath: [['\\(', '\\)']]
				}
			}

			var configScript = 'MathJax.Hub.Config(' + JSON.stringify(mathJaxConfig) + ');';
			var script = document.createElement('script');
			script.type = 'text/x-mathjax-config';
			script.textContent = configScript;
			document.head.appendChild(script);

			var mathJaxScript = document.createElement('script');
			mathJaxScript.id = 'mathJax';
			mathJaxScript.async = 'async';
			mathJaxScript.onload = function () {
				D2LMathML.ReadyState = 'ready';
			};
			mathJaxScript.src = (D2LMathML.IsLatex || renderLatex) ? latexUrl : mathMLUrl;
			document.head.appendChild(mathJaxScript);

		}.bind(this);

		if (isMathJaxLoaded()) {
			return;
		}

		if (isMathJaxRequired()) {
			loadMathJax();
		} else if (this.m_hasAfterPartialEvent() && !this.m_afterPartialHandler) {
			this.m_afterPartialHandler = function () {
				if (isMathJaxLoaded() || !isMathJaxRequired()) {
					return;
				}
				loadMathJax();
				D2L.LP.Web.UI.Html.PartialRendering.OnAfter.RemoveListener(this.m_afterPartialHandler);
				D2L.LP.Web.UI.Desktop.Controls.HtmlBlock.OnAfterRender.RemoveListener(this.m_afterPartialHandler);
				this.m_afterPartialHandler = null;
			}.bind(this);
			D2L.LP.Web.UI.Html.PartialRendering.OnAfter.AddListener(this.m_afterPartialHandler);
			D2L.LP.Web.UI.Desktop.Controls.HtmlBlock.OnAfterRender.AddListener(this.m_afterPartialHandler);
		}

	}
};