A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест;(function(d,e,c,r){e=d.documentElement;c="className";r="replace";e\[c\]=e\[c\]\[r\]("i-ua\_js\_no","i-ua\_js\_yes");if(d.compatMode!="CSS1Compat")e\[c\]=e\[c\]\[r\]("i-ua\_css\_standart","i-ua\_css\_quirks")})(document);;(function(d,e,c,n,w,v,f){e=d.documentElement;c="className";n="createElementNS";f="firstChild";w="http://www.w3.org/2000/svg";e\[c\]+=" i-ua\_svg\_"+(!!d\[n\]&&!!d\[n\](w,"svg").createSVGRect?"yes":"no");v=d.createElement("div");v.innerHTML="<svg/>";e\[c\]+=" i-ua\_inlinesvg\_"+((v\[f\]&&v\[f\].namespaceURI)==w?"yes":"no");})(document);;(function(d,e,p){e=d.documentElement;p="placeholder";e.className+=" i-ua\_"+p+(p in d.createElement("input")?"\_yes":"\_no")})(document);!function(n,i){if(n.Ya=n.Ya||{},Ya.Rum)throw new Error("Rum: interface is already defined");var e=n.performance,t=e&&e.timing&&e.timing.navigationStart||Ya.startPageLoad||+new Date,a=n.requestAnimationFrame,r=Ya.Rum={enabled:!!e,vsStart:document.visibilityState,vsChanged:!1,\_defTimes:\[\],\_defRes:\[\],\_deltaMarks:{},\_markListeners:{},\_onComplete:\[\],\_onInit:\[\],\_unsubscribers:\[\],\_settings:{},\_vars:{},init:function(n,i){r.\_settings=n,r.\_vars=i},getTime:e&&e.now?function(){return e.now()}:Date.now?function(){return Date.now()-t}:function(){return new Date-t},time:function(n){r.\_deltaMarks\[n\]=\[r.getTime()\]},timeEnd:function(n,i){var e=r.\_deltaMarks\[n\];e&&0!==e.length&&e.push(r.getTime(),i)},sendTimeMark:function(n,i,e,t){void 0===i&&(i=r.getTime()),r.\_defTimes.push(\[n,i,t\]),r.mark(n,i)},sendDelta:function(n,i,e,t){var a,s=r.\_deltaMarks;s\[n\]||void 0===i||(a=t&&t.originalEndTime?t.originalEndTime:r.getTime(),s\[n\]=\[a-i,a,e\])},sendResTiming:function(n,i){r.\_defRes.push(\[n,i\])},sendRaf:function(n){var i=r.getSetting("forcePaintTimeSending");if(a&&(i||!r.isVisibilityChanged())){var e="2616."+n;a((function(){!i&&r.isVisibilityChanged()||(r.getSetting("sendFirstRaf")&&r.sendTimeMark(e+".205"),a((function(){!i&&r.isVisibilityChanged()||r.sendTimeMark(e+".1928")})))}))}},isVisibilityChanged:function(){return r.vsStart&&("visible"!==r.vsStart||r.vsChanged)},mark:e&&e.mark?function(n,i){e.mark(n+(i?": "+i:""))}:function(){},getSetting:function(n){var i=r.\_settings\[n\];return null===i?null:i||""},on:function(n,i){if("function"==typeof i)return(r.\_markListeners\[n\]=r.\_markListeners\[n\]||\[\]).push(i),function(){if(r.\_markListeners\[n\]){var e=r.\_markListeners\[n\].indexOf(i);e>-1&&r.\_markListeners\[n\].splice(e,1)}}},sendTrafficData:function(){},finalizeLayoutShiftScore:function(){},finalizeLargestContentfulPaint:function(){},getLCPAdditionalParams:function(){}};document.addEventListener&&document.addEventListener("visibilitychange",(function n(){Ya.Rum.vsChanged=!0,document.removeEventListener("visibilitychange",n)}))}(window); !function(){if(window.PerformanceLongTaskTiming){var e=function(e,n){return(e=e.concat(n)).length>300&&(e=e.slice(e.length-300)),e};function n(){var n=Ya.Rum.\_tti={events:\[\],eventsAfterTTI:\[\],fired:!1,observer:new PerformanceObserver((function(r){var t=r.getEntries();n.events=e(n.events,t),n.fired&&(n.eventsAfterTTI=e(n.eventsAfterTTI,t))}))};n.observer.observe({entryTypes:\["longtask"\]}),Ya.Rum.\_unsubscribers&&Ya.Rum.\_unsubscribers.push((function(){n.observer.disconnect()}))}n(),Ya.Rum.\_onInit&&Ya.Rum.\_onInit.push(n)}}(); Ya.Rum.observeDOMNode=window.IntersectionObserver?function(e,i,n){var t=this,o=Ya.Rum.getSetting("forcePaintTimeSending");!function r(){if(o||!t.isVisibilityChanged()){var s="string"==typeof i?document.querySelector(i):i;s?new IntersectionObserver((function(i,n){!o&&t.isVisibilityChanged()||(Ya.Rum.sendTimeMark(e),n.unobserve(s))}),n).observe(s):setTimeout(r,100)}}()}:function(){}; !function(){var e,n,t,i=Ya.Rum,o=\[\];function s(){var t=o.join("\\r\\n");o=\[\],e=null,n&&a(n,t)}function a(e,n){if(!(navigator.sendBeacon&&t&&navigator.sendBeacon(e,n))){var i=new XMLHttpRequest;i.open("POST",e),i.send(n)}}function g(t,c,r,u,l,v,d,f,j,m){var p=\[t?"/reqid="+t:"",c?"/"+c.join("/"):"",r?"/path="+r:"",u?"/events="+u:"",l?"/slots="+l.join(";"):"",v?"/experiments="+v.join(";"):"",d?"/vars="+d:"","/cts="+(new Date).getTime(),j||"","/\*"+(f||"")\];m&&m!==n?a(m,p.join("")):(o.push(p.join("")),o.length<42?e=setTimeout(s,15):s(),i.sendToClck=g)}i.send=function(o,s,a,c,r,u,l){clearTimeout(e),n=i.getSetting("clck"),t=i.getSetting("beacon"),g(i.getSetting("reqid"),l,s,r,i.getSetting("slots"),i.getSetting("experiments"),a)}}(); !function(){var n=Ya.Rum,i=window.BEM;function t(){i&&i.channel("i-bem").onFirst("start-init",(function(){n.getSetting("sendBeforeBemInited")&&n.sendTimeMark("2418")})).onFirst("init",(function(){n.sendTimeMark("2295")}))}t(),n.\_onInit&&n.\_onInit.push(t)}(); Ya.Rum.init({"beacon":true,"clck":"https://yandex.ru/clck/click","reqid":"I2v6b9GP"}, {"-page":"unknown","-platform":"desktop","-env":"production","rum\_id":"ru.contest-www","-project":"contest-www"}); !function(e,n){if(!e)throw new Error("Rum: interface is not included");if(!e.enabled)return e.getSetting=function(){return""},e.getVarsList=function(){return\[\]},void(e.getResourceTimings=e.pushConnectionTypeTo=e.pushTimingTo=e.normalize=e.sendCounter=e.sendDelta=e.sendTimeMark=e.sendResTiming=e.sendTiming=e.sendTTI=e.makeSubPage=e.sendHeroElement=e.onReady=e.onQuietWindow=function(){});e.getVarsList=function(){var n=e.\_vars;return Object.keys(n).map(function(e){return e+"="+encodeURIComponent(n\[e\]).replace(/\\\*/g,"%2A")})},e.setVars=function(n){Object.keys(n).forEach(function(t){e.\_vars\[t\]=n\[t\]}),M(),I()};var t,i,r="690.1033",o="690.2096.207",a="690.2096.2877",s="690.2096.2892",c="690.2096.2044",u="690.2096.361",d="690.2096.4004",f=3,l=3e3,v={connectEnd:2116,connectStart:2114,decodedBodySize:2886,domComplete:2124,domContentLoadedEventEnd:2131,domContentLoadedEventStart:2123,domInteractive:2770,domLoading:2769,domainLookupEnd:2113,domainLookupStart:2112,duration:2136,encodedBodySize:2887,entryType:2888,fetchStart:2111,initiatorType:2889,loadEventEnd:2126,loadEventStart:2125,nextHopProtocol:2890,redirectCount:1385,redirectEnd:2110,redirectStart:2109,requestStart:2117,responseEnd:2120,responseStart:2119,secureConnectionStart:2115,startTime:2322,transferSize:2323,type:76,unloadEventEnd:2128,unloadEventStart:2127,workerStart:2137},g={visible:1,hidden:2,prerender:3},m={bluetooth:2064,cellular:2065,ethernet:2066,none:1229,wifi:2067,wimax:2068,other:861,unknown:836,0:836,1:2066,2:2067,3:2070,4:2071,5:2768},p={"first-paint":2793,"first-contentful-paint":2794},h=Object.keys(p).length,y=e.getTime,T=window.PerformanceObserver,E=window.performance||{},S=E.timing||{},b=E.navigation||{},C=navigator.connection,k={},L={},w=e.\_deltaMarks,R=document.createElement("link"),j=document.createElement("a"),x="function"==typeof E.getEntriesByType,\_=S.navigationStart;function M(){t=e.getVarsList(),e.getSetting("sendClientUa")&&t.push("1042="+encodeURIComponent(navigator.userAgent))}function I(){i=t.concat(\["143.2129="+\_\])}function O(e){function n(){removeEventListener("DOMContentLoaded",n),removeEventListener("load",n),e()}"loading"===document.readyState?(addEventListener("DOMContentLoaded",n),addEventListener("load",n)):e()}function z(){var n;e.getSetting("disableOnLoadTasks")||(removeEventListener("load",z),(n=e.getSetting("periodicStatsIntervalMs"))||null===n||(n=15e3),n&&(V=setInterval(Q,n)),addEventListener("beforeunload",Q),function(){if(T){q(E.getEntriesByType("navigation")),q(E.getEntriesByType("resource"));try{new T(function(e){q(e.getEntries())}).observe({entryTypes:\["resource","navigation"\]})}catch(e){}e.\_periodicTasks.push(J)}}(),function(){if(T)try{new T(function(e,n){var t=e.getEntries()\[0\];if(t){var i=t.processingStart,r={duration:t.duration,js:t.processingEnd-i,name:t.name};t.target&&(r.target=K(t.target)),A("first-input",i-t.startTime,r),n.disconnect()}}).observe({type:"first-input",buffered:!0})}catch(e){}}(),function(){if(x){var e=E.getEntriesByType("navigation")\[0\];if(e){var n=\[\];me(n,e),fe(n);var i=E.getEntriesByName("yndxNavigationSource")\[0\];i&&n.push("2091.186="+i.value),he(s,t.concat(n))}}}(),function(){if(T){var n=e.getSetting("clsWindowGap")?e.getSetting("clsWindowGap"):1/0,t=e.getSetting("clsWindowSize")?e.getSetting("clsWindowSize"):1/0,i=new T(function(e){var i=e.getEntries();null==$&&($=0);for(var r=0;r<i.length;r++){var o=i\[r\];o.hadRecentInput||(Z&&o.startTime-X\[X.length-1\].startTime<n&&o.startTime-X\[0\].startTime<t?(Z+=o.value,X.push(o)):(ne(),Z=o.value,X=\[o\]))}ne()});try{i.observe({type:"layout-shift",buffered:!0})}catch(e){}addEventListener("visibilitychange",function e(){if("hidden"===document.visibilityState){removeEventListener("visibilitychange",e);try{"function"==typeof i.takeRecords&&i.takeRecords(),i.disconnect()}catch(e){}te()}}),addEventListener("beforeunload",te)}}(),function(){if(T&&(e.getSetting("forcePaintTimeSending")||!e.isVisibilityChanged())){var n=new T(function(e){for(var n=e.getEntries(),t=0;t<n.length;t++){var i=n\[t\];ie=i.renderTime||i.loadTime,re=i}oe||(U("largest-loading-elem-paint",ie),oe=!0)});try{n.observe({type:"largest-contentful-paint",buffered:!0})}catch(e){}addEventListener("visibilitychange",function e(){if("hidden"===document.visibilityState){removeEventListener("visibilitychange",e);try{"function"==typeof n.takeRecords&&n.takeRecords(),n.disconnect()}catch(e){}ae()}}),addEventListener("beforeunload",ae)}}())}function B(){var n=S.domContentLoadedEventStart,i=S.domContentLoadedEventEnd;if(0!==n||0!==i){var o=0===S.responseStart?\_:S.responseStart,a=0===S.domainLookupStart?\_:S.domainLookupStart,s=t.concat(\["2129="+\_,"1036="+(a-\_),"1037="+(S.domainLookupEnd-S.domainLookupStart),"1038="+(S.connectEnd-S.connectStart),S.secureConnectionStart&&"1383="+(S.connectEnd-S.secureConnectionStart),"1039="+(S.responseStart-S.connectEnd),"1040="+(S.responseEnd-o),"1040.906="+(S.responseEnd-a),"1310.2084="+(S.domLoading-o),"1310.2085="+(S.domInteractive-o),"1310.1309="+(i-n),"1310.1007="+(n-o),navigator.deviceMemory&&"3140="+navigator.deviceMemory,navigator.hardwareConcurrency&&"3141="+navigator.hardwareConcurrency\]);Object.keys(v).forEach(function(e){e in S&&S\[e\]&&s.push(v\[e\]+"="+pe(S\[e\],\_))}),e.vsStart?(s.push("1484="+(g\[e.vsStart\]||2771)),e.vsChanged&&s.push("1484.719=1")):s.push("1484="+g.visible),b&&(b.redirectCount&&s.push("1384.1385="+b.redirectCount),1!==b.type&&2!==b.type||s.push("770.76="+b.type)),fe(s),he(r,s)}else setTimeout(B,50)}M(),I(),e.ajaxStart=0,e.ajaxComplete=0,O(function(){\_&&setTimeout(function(){e.sendTimeMark=U,e.sendResTiming=H,e.sendTiming=G,e.timeEnd=D;for(var n=e.\_defRes;n.length;){var t=n.shift();H(t\[0\],t\[1\])}for(var i=e.\_defTimes;i.length;){var r=i.shift();U(r\[0\],r\[1\],!1,r\[2\])}Object.keys(w).forEach(function(e){A(e)}),B(),function n(){if(x&&(e.getSetting("forcePaintTimeSending")||!e.isVisibilityChanged())){for(var t=E.getEntriesByType("paint"),i=0;i<t.length;i++){var r=t\[i\],o=p\[r.name\];o&&!P\[r.name\]&&(P\[r.name\]=!0,N++,U("1926."+o,r.startTime))}if(N<h)try{new T(function(e,t){n(),t&&t.disconnect()}).observe({entryTypes:\["paint"\]})}catch(e){}}}(),e.getSetting("sendAutoElementTiming")&&se(),window.addEventListener("pageshow",ce),ue(),"complete"===document.readyState?z():addEventListener("load",z)},0)}),e.\_getCommonVars=function(){return t};var V,P={},N=0;function U(t,i,r,a){i===n&&(i=y()),r!==n&&!0!==r||e.mark(t,i);var s=ge(t);if(s.push("207="+pe(i)),W(s,a)){he(o,s),k\[t\]=k\[t\]||\[\],k\[t\].push(i);var c=e.\_markListeners\[t\];c&&c.length&&c.forEach(function(e){e(i)})}}function W(e,t){if(t){if(t.isCanceled&&t.isCanceled())return!1;var i=e.reduce(function(e,n,t){return"string"==typeof n&&(e\[n.split("=")\[0\]\]=t),e},{});Object.keys(t).forEach(function(r){if("function"!=typeof t\[r\]){var o=i\[r\],a=r+"="+t\[r\];o===n?e.push(a):e\[o\]=a}})}return!0}function D(e,n){var t=w\[e\];t&&0!==t.length&&(t.push(y(),n),A(e))}function A(t,i,r,o){var s,c,u,d=w\[t\];if(void 0!==i?s=(c=o&&o.originalEndTime?o.originalEndTime:e.getTime())-i:d&&(s=d\[0\],c=d\[1\],u=d\[2\]),s!==n&&c!==n){var f=ge(t);f.push("207.2154="+pe(s),"207.1428="+pe(c),"2877="+pe(c-s)),W(f,r)&&W(f,u)&&(he(a,f),delete w\[t\])}}function H(e,n){le(n,function(t){t&&G(e,t\[t.length-1\],n)})}function G(n,t,i){var r=ge(n);e.getSetting("sendUrlInResTiming")&&r.push("13="+encodeURIComponent(i)),me(r,t),he(c,r)}function Q(){var n=!1;e.\_periodicTasks.forEach(function(e){e()&&(n=!0)}),n||clearInterval(V)}e.getTimeMarks=function(){return k},e.\_periodicTasks=\[\];var Y=0;function q(e){if(e&&e.length)for(var n=L,t=0;t<e.length;t++){var i=F(e\[t\]);if(i){var r=i.domain+"-"+i.extension,o=n\[r\]=n\[r\]||{count:0,size:0};o.count++,o.size+=i.size}}}function F(e){var n=e.transferSize;if(null!=n){j.href=e.name;var t=j.pathname;if(0!==t.indexOf("/clck")){var i=t.lastIndexOf("."),r="";return-1!==i&&t.lastIndexOf("/")<i&&t.length-i<=5&&(r=t.slice(i+1)),{size:n,domain:j.hostname,extension:r}}}}function J(){var n=e.getSetting("maxTrafficCounters")||250;if(Y>=n)return!1;for(var i=Object.keys(L),r="",o=0;o<i.length;o++){var a=i\[o\],s=L\[a\];r+=encodeURIComponent(a)+"!"+s.count+"!"+s.size+";"}if(r.length){Y++;var c=t.concat(\["d="+r,"t="+pe(y())\]);he(u,c)}return L={},Y<n}function K(e){if(!e)return"";var t=(e.tagName||"").toLowerCase(),i=e.className&&e.className.baseVal!==n?e.className.baseVal:e.className;return t+(i?(" "+i).replace(/\\s+/g,"."):"")}var X,Z,$=("layout-shift",Boolean(T&&T.supportedEntryTypes&&-1!==T.supportedEntryTypes.indexOf("layout-shift"))?0:null),ee=null;function ne(){Z>$&&($=Z,ee=X)}function te(){if(null!=$){var i=\["s="+Math.round(1e6\*$)/1e6\];if(e.getSetting("logClsTarget")){var r=function(e){var n=null;if(!e)return null;var t=null;return(n=e.reduce(function(e,n){return e&&e.value>n.value?e:n}))&&n.sources&&n.sources.length&&(t=n.sources.find(function(e){return e.node&&1===e.node.nodeType})||n.sources\[0\]),t&&K(t.node)}(ee);i.push("target="+r)}he(d,t.concat(i)),$=null,Z=n,X=n}}var ie=null,re=null,oe=!1;function ae(){if(null!=ie){var n=e.getLCPAdditionalParams(re);U("largest-contentful-paint",ie,!1,n),ie=null,re=null}}var se=T?function(){if(e.getSetting("forcePaintTimeSending")||!e.isVisibilityChanged())try{new T(function(e){for(var n=e.getEntries(),t=0;t<n.length;t++){var i=n\[t\];U("element-timing."+i.identifier,i.startTime)}}).observe({type:"element",buffered:!0})}catch(e){}}:function(){};function ce(e){e.persisted&&U("bfcache")}function ue(n,t,i){if(e.\_tti){var r=y();de(function(o){var a={2796.2797:ve(e.\_tti.events||\[\],t),689.2322:pe(r)};i&&Object.keys(i).forEach(function(e){a\[e\]=i\[e\]}),U(n||"2795",o,!0,a),e.\_tti.fired=!0},t)}}function de(n,t){e.\_tti&&(t||(t=y()),function i(){var r,o=t,a=y(),s=e.\_tti.events||\[\],c=s.length;0!==c&&(r=s\[c-1\],o=Math.max(o,Math.floor(r.startTime+r.duration))),a-o>=l?n(o):setTimeout(i,1e3)}())}function fe(e){C&&e.push("2437="+(m\[C.type\]||2771),C.downlinkMax!==n&&"2439="+C.downlinkMax,C.effectiveType&&"2870="+C.effectiveType,C.rtt!==n&&"rtt="+C.rtt,C.downlink!==n&&"dwl="+C.downlink)}function le(e,n){if(!x)return n(null);R.href=e;var t=R.href,i=0,r=100;setTimeout(function e(){var o=E.getEntriesByName(t);if(o.length)return n(o);i++<f?(setTimeout(e,r),r+=r):n(null)},0)}function ve(e,n){return e=e||\[\],n=n||0,e.filter(function(e){return e.startTime-n>=-50}).map(function(e){var n=e.name?e.name.split("-").map(function(e){return e\[0\]}).join(""):"u",t=Math.floor(e.startTime);return n+"-"+t+"-"+Math.floor(t+e.duration)}).join(".")}function ge(n){return i.concat(\["1701="+n,e.ajaxStart&&"1201.2154="+pe(e.ajaxStart),e.ajaxComplete&&"1201.2052="+pe(e.ajaxComplete)\])}function me(e,n){Object.keys(v).forEach(function(t){if(t in n){var i=n\[t\];(i||0===i)&&e.push(v\[t\]+"="+pe(i))}})}function pe(e,n){return"string"==typeof e?encodeURIComponent(e):Math.round(1e3\*(e-(n||0)))/1e3}function he(n,t){var i=encodeURIComponent(window.YaStaticRegion||"unknown");t.push("-cdn="+i);var r=t.filter(Boolean).join(",");e.send(null,n,r)}e.sendTTI=ue,e.sendHeroElement=function(e){U("2876",e)},e.\_subpages={},e.makeSubPage=function(n,t){var i=e.\_subpages\[n\];e.\_subpages\[n\]=void 0===i?i=0:++i;var r=!1;return{689.2322:pe(void 0!==t?t:y()),2924:n,2925:i,isCanceled:function(){return r},cancel:function(){r=!0}}},e.\_getLongtasksStringValue=ve,e.getResourceTimings=le,e.pushConnectionTypeTo=fe,e.pushTimingTo=me,e.normalize=pe,e.sendCounter=he,e.sendDelta=A,e.sendTrafficData=J,e.finalizeLayoutShiftScore=te,e.finalizeLargestContentfulPaint=ae,e.onReady=O,e.onQuietWindow=de,e.getSelector=K,e.sendBFCacheTimeMark=ce}(Ya.Rum); !function(n){if(!n.Ya||!Ya.Rum)throw new Error("Rum: interface is not defined");var e=Ya.Rum;e.getSetting=function(n){var t=e.\_settings\[n\];return null===t?null:t||""}}("undefined"!=typeof self?self:window); !function(e,r){var n={client:\["690.2354",1e3,100,0\],uncaught:\["690.2361",100,10,0\],external:\["690.2854",100,10,0\],script:\["690.2609",100,10,0\]},t={};r.ERROR\_LEVEL={INFO:"info",DEBUG:"debug",WARN:"warn",ERROR:"error",FATAL:"fatal"},r.\_errorSettings={clck:"https://yandex.ru/clck/click",beacon:!0,project:"unknown",page:"",env:"",experiments:\[\],additional:{},platform:"",region:"",dc:"",host:"",service:"",level:"",version:"",yandexuid:"",loggedin:!1,coordinates\_gp:"",referrer:!0,preventError:!1,unhandledRejection:!1,traceUnhandledRejection:!1,uncaughtException:!0,debug:!1,limits:{},silent:{},filters:{},pageMaxAge:864e6,initTimestamp:+new Date};var o=!1;function a(e,r){for(var n in r)r.hasOwnProperty(n)&&(e\[n\]=r\[n\]);return e}function i(e){return"boolean"==typeof e&&(e=+e),"number"==typeof e?e+"":null}r.initErrors=function(n){var t=a(r.\_errorSettings,n);o||(t.uncaughtException&&function(){var n=r.\_errorSettings;if(e.addEventListener)e.addEventListener("error",s),n.resourceFails&&e.addEventListener("error",l,!0),"Promise"in e&&n.unhandledRejection&&e.addEventListener("unhandledrejection",function(e){var n,t,o=e.reason,a={};o&&(o.stack&&o.message?(n=o.message,t=o.stack):(n=String(o),t=r.\_parseTraceablePromiseStack(e.promise),"\[object Event\]"===n?n="event.type: "+o.type:"\[object Object\]"===n&&(a.unhandledObject=o)),o.target&&o.target.src&&(a.src=o.target.src),s({message:"Unhandled rejection: "+n,stack:t,additional:a}))});else{var t=e.onerror;e.onerror=function(e,r,n,o,a){s({error:a||new Error(e||"Empty error"),message:e,lineno:n,colno:o,filename:r}),t&&t.apply(this,arguments)}}}(),t.unhandledRejection&&t.traceUnhandledRejection&&r.\_traceUnhandledRejection&&r.\_traceUnhandledRejection(),o=!0)},r.updateErrors=function(e){a(r.\_errorSettings,e)},r.updateAdditional=function(e){r.\_errorSettings.additional=a(r.\_errorSettings.additional||{},e)},r.\_handleError=function(e,o,i){var s,l,c=r.\_errorSettings;if(c.preventError&&e.preventDefault&&e.preventDefault(),o)s=e,l="client";else{s=r.\_normalizeError(e),l=s.type;var d=c.onError;"function"==typeof d&&d(s);var u=c.transform;if("function"==typeof u&&(s=u(s)),!s)return;s.settings&&(i=s.settings)}var g=+new Date,f=c.initTimestamp,p=c.pageMaxAge;if(!(-1!==p&&f&&f+p<g)){var m=n\[l\]\[1\];"number"==typeof c.limits\[l\]&&(m=c.limits\[l\]);var v=n\[l\]\[2\];"number"==typeof c.silent\[l\]&&(v=c.silent\[l\]);var h=n\[l\]\[3\];if(h<m||-1===m){s.path=n\[l\]\[0\];var E=r.\_getErrorData(s,{silent:h<v||-1===v?"no":"yes",isCustom:Boolean(o)},a(a({},c),i)),\_=function(e){t\[s.message\]=!1,r.\_sendError(e.path,e.vars),n\[l\]\[3\]++}.bind(this,E);if(void 0===c.throttleSend)\_();else{if(t\[s.message\])return;t\[s.message\]=!0,setTimeout(\_,c.throttleSend)}}}},r.\_getReferrer=function(r){var n=r.referrer,t=typeof n;return"function"===t?n():"string"===t&&n?n:!1!==n&&e.location?e.location.href:void 0},r.getErrorSetting=function(e){return r.\_errorSettings\[e\]},r.\_buildExperiments=function(e){return e instanceof Array?e.join(";"):""},r.\_buildAdditional=function(e,r){var n="";try{var t=a(a({},e),r);0!==Object.keys(t).length&&(n=JSON.stringify(t))}catch(e){}return n},r.\_getErrorData=function(n,t,o){t=t||{};var a=r.\_buildExperiments(o.experiments),s=r.\_buildAdditional(o.additional,n.additional),l={"-stack":n.stack,"-url":n.file,"-line":n.line,"-col":n.col,"-block":n.block,"-method":n.method,"-msg":n.message,"-env":o.env,"-external":n.external,"-externalCustom":n.externalCustom,"-project":o.project,"-service":n.service||o.service,"-page":n.page||o.page,"-platform":o.platform,"-level":n.level,"-experiments":a,"-version":o.version,"-region":o.region,"-dc":o.dc,"-host":o.host,"-yandexuid":o.yandexuid,"-loggedin":o.loggedin,"-coordinates\_gp":n.coordinates\_gp||o.coordinates\_gp,"-referrer":r.\_getReferrer(o),"-source":n.source,"-sourceMethod":n.sourceMethod,"-type":t.isCustom?n.type:"","-additional":s,"-adb":i(Ya.blocker)||i(o.blocker),"-cdn":e.YaStaticRegion,"-ua":navigator.userAgent,"-silent":t.silent,"-ts":+new Date,"-init-ts":o.initTimestamp};return o.debug&&e.console&&console\[console\[n.level\]?n.level:"error"\]("\[error-counter\] "+n.message,l,n.stack),{path:n.path,vars:l}},r.\_baseNormalizeError=function(e){var r=(e=e||{}).error,n=e.filename||e.fileName||"",t=r&&r.stack||e.stack||"",o=e.message||"",a=r&&r.additional||e.additional;return{file:n,line:e.lineno||e.lineNumber,col:e.colno||e.colNumber,stack:t,message:o,additional:a}},r.\_normalizeError=function(e){var n=r.\_baseNormalizeError(e),t="uncaught",o=r.\_isExternalError(n.file,n.message,n.stack),a="",i="";return o.hasExternal?(t="external",a=o.common,i=o.custom):/^Script error\\.?$/.test(n.message)&&(t="script"),n.external=a,n.externalCustom=i,n.type=t,n},r.\_createVarsString=function(e){var r=\[\];for(var n in e)e.hasOwnProperty(n)&&(e\[n\]||0===e\[n\])&&r.push(n+"="+encodeURIComponent(e\[n\]).replace(/\\\*/g,"%2A"));return r.join(",")},r.\_sendError=function(e,n){r.send(null,e,r.\_createVarsString(n),null,null,null,null)};var s=function(e){r.\_handleError(e,!1)},l=function(e){var n=e.target;if(n){var t=n.srcset||n.src;if(t||(t=n.href),t){var o=n.tagName||"UNKNOWN";r.logError({message:o+" load error",additional:{src:t}})}}};r.\_parseTraceablePromiseStack=function(){}}("undefined"!=typeof self?self:window,Ya.Rum); !function(e){var r={url:{0:/(miscellaneous|extension)\_bindings/,1:/^chrome:/,2:/kaspersky-labs\\.com\\//,3:/^(?:moz|chrome|safari)-extension:\\/\\//,4:/^file:/,5:/^resource:\\/\\//,6:/webnetc\\.top/,7:/local\\.adguard\\.com/},message:{0:/\_\_adgRemoveDirect/,1:/Content Security Policy/,2:/vid\_mate\_check/,3:/ucapi/,4:/Access is denied/i,5:/^Uncaught SecurityError/i,6:/\_\_ybro/,7:/\_\_show\_\_deepen/,8:/ntp is not defined/,9:/Cannot set property 'install' of undefined/,10:/NS\_ERROR/,11:/Error loading script/,12:/^TypeError: undefined is not a function$/,13:/\_\_firefox\_\_\\.(?:favicons|metadata|reader|searchQueryForField|searchLoginField)/},stack:{0:/(?:moz|chrome|safari)-extension:\\/\\//,1:/adguard.\*\\.user\\.js/i}};function n(e,r){if(e&&r){var n=\[\];for(var o in r)if(r.hasOwnProperty(o)){var i=r\[o\];"string"==typeof i&&(i=new RegExp(i)),i instanceof RegExp&&i.test(e)&&n.push(o)}return n.join("\_")}}function o(e,o){var i,a=\[\];for(var t in r)r.hasOwnProperty(t)&&(i=n(e\[t\],o\[t\]))&&a.push(t+"~"+i);return a.join(";")}e.\_isExternalError=function(n,i,a){var t=e.\_errorSettings.filters||{},s={url:(n||"")+"",message:(i||"")+"",stack:(a||"")+""},c=o(s,r),u=o(s,t);return{common:c,custom:u,hasExternal:!(!c&&!u)}}}(Ya.Rum); Ya.Rum.initErrors({"page":"unknown","platform":"desktop","env":"production","reqid":"I2v6b9GP","project":"contest-www"});window.MathJax = { AssistiveMML: { disabled: true }, showMathMenu: false };.MathJax\_Hover\_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute} .MathJax\_Menu\_Button .MathJax\_Hover\_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0} .MathJax\_Menu\_Button .MathJax\_Hover\_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px} .MathJax\_Hover\_Arrow:hover {color: white!important; border: 2px solid #CCC!important} .MathJax\_Hover\_Arrow:hover span {background-color: #CCC!important} #MathJax\_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')} #MathJax\_About.MathJax\_MousePost {outline: none} .MathJax\_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')} .MathJax\_MenuItem {padding: 2px 2em; background: transparent} .MathJax\_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em} .MathJax\_MenuActive .MathJax\_MenuArrow {color: white} .MathJax\_MenuArrow.RTL {left: .5em; right: auto} .MathJax\_MenuCheck {position: absolute; left: .7em} .MathJax\_MenuCheck.RTL {right: .7em; left: auto} .MathJax\_MenuRadioCheck {position: absolute; left: 1em} .MathJax\_MenuRadioCheck.RTL {right: 1em; left: auto} .MathJax\_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic} .MathJax\_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px} .MathJax\_MenuDisabled {color: GrayText} .MathJax\_MenuActive {background-color: Highlight; color: HighlightText} .MathJax\_MenuDisabled:focus, .MathJax\_MenuLabel:focus {background-color: #E8E8E8} .MathJax\_ContextMenu:focus {outline: none} .MathJax\_ContextMenu .MathJax\_MenuItem:focus {outline: none} #MathJax\_AboutClose {top: .2em; right: .2em} .MathJax\_Menu .MathJax\_MenuClose {top: -10px; left: -10px} .MathJax\_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0} .MathJax\_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px} .MathJax\_MenuClose:hover {color: white!important; border: 2px solid #CCC!important} .MathJax\_MenuClose:hover span {background-color: #CCC!important} .MathJax\_MenuClose:hover:focus {outline: none} .MathJax\_Preview .MJXf-math {color: inherit!important} .MJX\_Assistive\_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none} .MJX\_Assistive\_MathML.MJX\_Assistive\_MathML\_Block {width: 100%!important} #MathJax\_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')} #MathJax\_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)} #MathJax\_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0} #MathJax\_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)} .MathJax\_Preview {color: #888} #MathJax\_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap} #MathJax\_MSIE\_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px} .MathJax\_Error {color: #CC0000; font-style: italic} .u8n8V1CYJG6ACDwa777w{position:absolute;display:block;width:16px;height:16px;font-size:0;background-repeat:no-repeat;background-position:50% 50%;border-radius:50%}.u8n8V1CYJG6ACDwa777w:after{position:absolute;content:"";width:44px;height:26px;left:-20px;top:-8px}.u8n8V1CYJG6ACDwa777w:hover{cursor:pointer;background-color:var(--color-close-hover-bg)}.dzCDBUAznXSxVdGj1S7X{--thick-popup-offset: 16px;--horiz-shift: -100vw;--vert-shift: -100vh}.dzCDBUAznXSxVdGj1S7X{height:auto;background:var(--color-content-bg);border-radius:16px;pointer-events:none;z-index:9999}.dzCDBUAznXSxVdGj1S7X.fL5Owfu9xYWrxSlFekwz{position:absolute}.dzCDBUAznXSxVdGj1S7X.tFVNFALE8CgbdkspQgXJ{position:fixed}.dzCDBUAznXSxVdGj1S7X.TZbANCRE7ej6hWXvm4sw{left:var(--horiz-shift)}.dzCDBUAznXSxVdGj1S7X.sLWfm6BmA5C2rP8RH2lh{right:var(--horiz-shift)}.dzCDBUAznXSxVdGj1S7X.zyUt1ulGu7Lctcqt9Wwb{top:var(--vert-shift)}.dzCDBUAznXSxVdGj1S7X.NFKvx2noTZuUABoQOIgw{bottom:var(--vert-shift)}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA{top:var(--vert-shift);left:var(--horiz-shift)}.dzCDBUAznXSxVdGj1S7X.NFKvx2noTZuUABoQOIgw.dzCDBUAznXSxVdGj1S7X.fL5Owfu9xYWrxSlFekwz{--vert-shift: 0}.yP6u\_4fglSQcvruyoYvp{pointer-events:all;z-index:9999}.yP6u\_4fglSQcvruyoYvp.dzCDBUAznXSxVdGj1S7X{transition:left .5s,right .5s,top .5s,bottom .5s ease-out}.FJkGA3xCbqzGT0n2EMy7{margin-left:auto;position:relative;box-shadow:0px 8px 40px 0px rgba(33,32,31,.12);border-radius:16px}.A9lP13CP5JmkdVp3aYdq{min-height:36px;background:var(--color-header-popup-bg) 50% 50% no-repeat;background-size:100px;border-radius:16px 16px 0 0}.A9lP13CP5JmkdVp3aYdq.hoQR6MQKQAxgFUvjJ3vC{display:none}.h4aXscBoDD4zSt5DFRwg.hoQR6MQKQAxgFUvjJ3vC{border-radius:16px}.h4aXscBoDD4zSt5DFRwg{overflow:hidden;border-radius:0px 0px 16px 16px;background:var(--color-content-bg)}.h4aXscBoDD4zSt5DFRwg.hoQR6MQKQAxgFUvjJ3vC iframe{border-radius:16px}.h4aXscBoDD4zSt5DFRwg iframe{display:block;border:0;overflow:hidden;border-radius:0 0 16px 16px;width:320px}.h4aXscBoDD4zSt5DFRwg iframe.XsSKBX1\_k9QpApPDM1zs{width:calc(100vw - 2\*var(--thick-popup-offset))}.Fpgt\_Kf0hCJU1CoBT8fx{top:8px;right:8px}@media(max-width: 500px){.dzCDBUAznXSxVdGj1S7X.yP6u\_4fglSQcvruyoYvp{--horiz-shift: 16px}.dzCDBUAznXSxVdGj1S7X.NFKvx2noTZuUABoQOIgw.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6,.dzCDBUAznXSxVdGj1S7X.zyUt1ulGu7Lctcqt9Wwb.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--vert-shift: 12px}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--vert-shift: 50%;transform:translate(0%, -50%)}.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6 .h4aXscBoDD4zSt5DFRwg iframe{transition:height .3s}.dzCDBUAznXSxVdGj1S7X.NFKvx2noTZuUABoQOIgw.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3,.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3{top:12px;bottom:unset}.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3 .h4aXscBoDD4zSt5DFRwg iframe{transition:none}}@media(min-width: 501px){.dzCDBUAznXSxVdGj1S7X.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--horiz-shift: 30px;--vert-shift: 30px}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--horiz-shift: 50%;--vert-shift: 50%;transform:translate(-50%, -50%)}.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6 .h4aXscBoDD4zSt5DFRwg iframe{transition:height .3s}.dzCDBUAznXSxVdGj1S7X.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3{top:10px;bottom:unset;--horiz-shift: 30px}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3{--horiz-shift: 50%;transform:translate(-50%, 0%)}.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3 .h4aXscBoDD4zSt5DFRwg iframe{transition:none}}@media(orientation: landscape)and (max-device-width: 500px){.dzCDBUAznXSxVdGj1S7X.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3{top:10px;bottom:unset;--horiz-shift: 10px}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.AxucLDsdelBla\_Bw3Fn3{--horiz-shift: 50%;transform:translate(-50%, 0%)}.dzCDBUAznXSxVdGj1S7X.sr2JfeVqmXom70U3vKtA.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--horiz-shift: 50%;--vert-shift: 50%;transform:translate(-50%, -50%)}.dzCDBUAznXSxVdGj1S7X.yP6u\_4fglSQcvruyoYvp.Y0n9jC\_RhNVMcgcYWrA6{--horiz-shift: 10px;--vert-shift: 10px}}.qbORpikLObufPvziZ9y\_{position:fixed;top:0;left:0;right:0;bottom:0;height:auto;transition:.5s all;z-index:9999;pointer-events:all;background-color:rgba(0,0,0,.25)}.hHnggwS8sytaHsy6fuWZ{position:relative;left:50%;top:50%;width:545px;max-width:100%;transform:translate(-50%, -50%);border-radius:16px;box-shadow:0px 4px 7px rgba(0,0,0,.25);background-color:var(--color-content-bg)}.wEOFUiLOfluq86BrDUfg{min-height:42px;border-radius:16px 16px 0px 0px;background:var(--color-header-modal-bg) 50% 55% no-repeat;background-size:132px}.wEOFUiLOfluq86BrDUfg.\_2M3fKxqWmql09JUCBEg{display:none}.fp0QgCrX1y48p3elvLVi{overflow:hidden;background:var(--color-content-bg);border-radius:0px 0px 16px 16px;height:auto}.fp0QgCrX1y48p3elvLVi.\_2M3fKxqWmql09JUCBEg{border-radius:16px}.fp0QgCrX1y48p3elvLVi iframe{display:block;border:0;overflow:auto;width:100%}.Phidw\_u4HJIdFwFJpWzG{top:12px;right:12px}@media(max-height: 669px)and (min-height: 370px){.fp0QgCrX1y48p3elvLVi iframe{min-height:320px}}@media(min-height: 670px){.fp0QgCrX1y48p3elvLVi iframe{min-height:620px}}body.ya-feedback\_\_modal\_open { overflow: hidden; } .j9B7up68rde9UJix2n7v{cursor:pointer;pointer-events:all}.j9B7up68rde9UJix2n7v a{font-size:14px;font-weight:400;font-family:Open Sans,sans-serif;position:fixed;z-index:1000;padding:10px 18px 25px 12px;height:0px;background-color:#f0f0f0;color:rgba(0,0,0,.85);box-shadow:0px 4px 7px rgba(0,0,0,.25)}.j9B7up68rde9UJix2n7v.mnuHg\_VGaA9cmuJ7Fjgw a,.j9B7up68rde9UJix2n7v.GaiCtmG9gshFjfLqdzeG a,.j9B7up68rde9UJix2n7v.AIfawx9HF4cM9LuOMt0k a{border-radius:8px 8px 0 0}.j9B7up68rde9UJix2n7v.b2ZKP3R8L2SZ3UdAXICQ a{border-radius:0 0 8px 8px;box-shadow:0px 4px 7px rgba(0,0,0,.25)}.j9B7up68rde9UJix2n7v.GaiCtmG9gshFjfLqdzeG a{right:-64px;transform:rotate(-90deg)}.j9B7up68rde9UJix2n7v.GaiCtmG9gshFjfLqdzeG.fMuOOsa1oUBWZbZ3oXnV a{right:-56px}.j9B7up68rde9UJix2n7v.mnuHg\_VGaA9cmuJ7Fjgw a{left:-64px;transform:rotate(90deg)}.j9B7up68rde9UJix2n7v.mnuHg\_VGaA9cmuJ7Fjgw.fMuOOsa1oUBWZbZ3oXnV a{left:-56px}.j9B7up68rde9UJix2n7v.AIfawx9HF4cM9LuOMt0k a{bottom:0px}.j9B7up68rde9UJix2n7v.b2ZKP3R8L2SZ3UdAXICQ a{top:0px}.j9B7up68rde9UJix2n7v.AIfawx9HF4cM9LuOMt0k a,.j9B7up68rde9UJix2n7v.b2ZKP3R8L2SZ3UdAXICQ a{left:0;right:0;margin:auto;width:134px}@media(max-width: 480px){.j9B7up68rde9UJix2n7v.GaiCtmG9gshFjfLqdzeG a,.j9B7up68rde9UJix2n7v.mnuHg\_VGaA9cmuJ7Fjgw a{bottom:150px}}@media(min-width: 481px){.j9B7up68rde9UJix2n7v.GaiCtmG9gshFjfLqdzeG a,.j9B7up68rde9UJix2n7v.mnuHg\_VGaA9cmuJ7Fjgw a{top:200px}}.sftrMRAIFtK\_kVzdUSLs\[data-theme=light\]{--color-header-popup-bg: #ffffff;--color-header-modal-bg: #ffffff;--color-content-bg: #fff;--color-close-cross: rgba(0, 0, 0, 0.3);--color-close-hover-bg: rgba(209, 209, 209, 1)}.sftrMRAIFtK\_kVzdUSLs\[data-theme=dark\]{--color-header-popup-bg: #677a9e33;--color-header-modal-bg: #677a9e33;--color-content-bg: rgba(50, 49, 53, 1);--color-close-cross: rgba(255, 255, 255, 0.3);--color-close-hover-bg: rgba(255, 255, 255, 0.12)}.sftrMRAIFtK\_kVzdUSLs{overflow-x:hidden;width:100%;height:100%;position:relative}.gWQ6kLPL\_6XKDUip4ZQN{width:100vw;height:100vh;max-width:100%;position:absolute;top:0;left:0;pointer-events:none}.qUmstruTeB5JYz66X8oS{position:absolute;visibility:hidden;width:100%;height:1px;left:0;top:0}.MJXp-script {font-size: .8em} .MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right} .MJXp-bold {font-weight: bold} .MJXp-italic {font-style: italic} .MJXp-scr {font-family: MathJax\_Script,'Times New Roman',Times,STIXGeneral,serif} .MJXp-frak {font-family: MathJax\_Fraktur,'Times New Roman',Times,STIXGeneral,serif} .MJXp-sf {font-family: MathJax\_SansSerif,'Times New Roman',Times,STIXGeneral,serif} .MJXp-cal {font-family: MathJax\_Caligraphic,'Times New Roman',Times,STIXGeneral,serif} .MJXp-mono {font-family: MathJax\_Typewriter,'Times New Roman',Times,STIXGeneral,serif} .MJXp-largeop {font-size: 150%} .MJXp-largeop.MJXp-int {vertical-align: -.2em} .MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse} .MJXp-display {display: block; text-align: center; margin: 1em 0} .MJXp-math span {display: inline-block} .MJXp-box {display: block!important; text-align: center} .MJXp-box:after {content: " "} .MJXp-rule {display: block!important; margin-top: .1em} .MJXp-char {display: block!important} .MJXp-mo {margin: 0 .15em} .MJXp-mfrac {margin: 0 .125em; vertical-align: .25em} .MJXp-denom {display: inline-table!important; width: 100%} .MJXp-denom > \* {display: table-row!important} .MJXp-surd {vertical-align: top} .MJXp-surd > \* {display: block!important} .MJXp-script-box > \* {display: table!important; height: 50%} .MJXp-script-box > \* > \* {display: table-cell!important; vertical-align: top} .MJXp-script-box > \*:last-child > \* {vertical-align: bottom} .MJXp-script-box > \* > \* > \* {display: block!important} .MJXp-mphantom {visibility: hidden} .MJXp-munderover {display: inline-table!important} .MJXp-over {display: inline-block!important; text-align: center} .MJXp-over > \* {display: block!important} .MJXp-munderover > \* {display: table-row!important} .MJXp-mtable {vertical-align: .25em; margin: 0 .125em} .MJXp-mtable > \* {display: inline-table!important; vertical-align: middle} .MJXp-mtr {display: table-row!important} .MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em} .MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0} .MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0} .MJXp-mlabeledtr {display: table-row!important} .MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0} .MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0} .MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%} .MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)} .MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)} .MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)} .MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)} .MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)} .MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)} .MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)} .MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)} .MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)} .MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)} .mjx-chtml {display: inline-block; line-height: 0; text-indent: 0; text-align: left; text-transform: none; font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; letter-spacing: normal; word-wrap: normal; word-spacing: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; margin: 0; padding: 1px 0} .MJXc-display {display: block; text-align: center; margin: 1em 0; padding: 0} .mjx-chtml\[tabindex\]:focus, body :focus .mjx-chtml\[tabindex\] {display: inline-table} .mjx-full-width {text-align: center; display: table-cell!important; width: 10000em} .mjx-math {display: inline-block; border-collapse: separate; border-spacing: 0} .mjx-math \* {display: inline-block; -webkit-box-sizing: content-box!important; -moz-box-sizing: content-box!important; box-sizing: content-box!important; text-align: left} .mjx-numerator {display: block; text-align: center} .mjx-denominator {display: block; text-align: center} .MJXc-stacked {height: 0; position: relative} .MJXc-stacked > \* {position: absolute} .MJXc-bevelled > \* {display: inline-block} .mjx-stack {display: inline-block} .mjx-op {display: block} .mjx-under {display: table-cell} .mjx-over {display: block} .mjx-over > \* {padding-left: 0px!important; padding-right: 0px!important} .mjx-under > \* {padding-left: 0px!important; padding-right: 0px!important} .mjx-stack > .mjx-sup {display: block} .mjx-stack > .mjx-sub {display: block} .mjx-prestack > .mjx-presup {display: block} .mjx-prestack > .mjx-presub {display: block} .mjx-delim-h > .mjx-char {display: inline-block} .mjx-surd {vertical-align: top} .mjx-mphantom \* {visibility: hidden} .mjx-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 2px 3px; font-style: normal; font-size: 90%} .mjx-annotation-xml {line-height: normal} .mjx-menclose > svg {fill: none; stroke: currentColor} .mjx-mtr {display: table-row} .mjx-mlabeledtr {display: table-row} .mjx-mtd {display: table-cell; text-align: center} .mjx-label {display: table-row} .mjx-box {display: inline-block} .mjx-block {display: block} .mjx-span {display: inline} .mjx-char {display: block; white-space: pre} .mjx-itable {display: inline-table; width: auto} .mjx-row {display: table-row} .mjx-cell {display: table-cell} .mjx-table {display: table; width: 100%} .mjx-line {display: block; height: 0} .mjx-strut {width: 0; padding-top: 1em} .mjx-vsize {width: 0} .MJXc-space1 {margin-left: .167em} .MJXc-space2 {margin-left: .222em} .MJXc-space3 {margin-left: .278em} .mjx-chartest {display: block; visibility: hidden; position: absolute; top: 0; line-height: normal; font-size: 500%} .mjx-chartest .mjx-char {display: inline} .mjx-chartest .mjx-box {padding-top: 1000px} .MJXc-processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden} .MJXc-processed {display: none} .mjx-test {display: block; font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px} .mjx-ex-box-test {position: absolute; width: 1px; height: 60ex} .mjx-line-box-test {display: table!important} .mjx-line-box-test span {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0} #MathJax\_CHTML\_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none} .MJXc-TeX-unknown-R {font-family: STIXGeneral,'Cambria Math','Arial Unicode MS',serif; font-style: normal; font-weight: normal} .MJXc-TeX-unknown-I {font-family: STIXGeneral,'Cambria Math','Arial Unicode MS',serif; font-style: italic; font-weight: normal} .MJXc-TeX-unknown-B {font-family: STIXGeneral,'Cambria Math','Arial Unicode MS',serif; font-style: normal; font-weight: bold} .MJXc-TeX-unknown-BI {font-family: STIXGeneral,'Cambria Math','Arial Unicode MS',serif; font-style: italic; font-weight: bold} .MJXc-TeX-ams-R {font-family: MJXc-TeX-ams-R,MJXc-TeX-ams-Rw} .MJXc-TeX-cal-B {font-family: MJXc-TeX-cal-B,MJXc-TeX-cal-Bx,MJXc-TeX-cal-Bw} .MJXc-TeX-frak-R {font-family: MJXc-TeX-frak-R,MJXc-TeX-frak-Rw} .MJXc-TeX-frak-B {font-family: MJXc-TeX-frak-B,MJXc-TeX-frak-Bx,MJXc-TeX-frak-Bw} .MJXc-TeX-math-BI {font-family: MJXc-TeX-math-BI,MJXc-TeX-math-BIx,MJXc-TeX-math-BIw} .MJXc-TeX-sans-R {font-family: MJXc-TeX-sans-R,MJXc-TeX-sans-Rw} .MJXc-TeX-sans-B {font-family: MJXc-TeX-sans-B,MJXc-TeX-sans-Bx,MJXc-TeX-sans-Bw} .MJXc-TeX-sans-I {font-family: MJXc-TeX-sans-I,MJXc-TeX-sans-Ix,MJXc-TeX-sans-Iw} .MJXc-TeX-script-R {font-family: MJXc-TeX-script-R,MJXc-TeX-script-Rw} .MJXc-TeX-type-R {font-family: MJXc-TeX-type-R,MJXc-TeX-type-Rw} .MJXc-TeX-cal-R {font-family: MJXc-TeX-cal-R,MJXc-TeX-cal-Rw} .MJXc-TeX-main-B {font-family: MJXc-TeX-main-B,MJXc-TeX-main-Bx,MJXc-TeX-main-Bw} .MJXc-TeX-main-I {font-family: MJXc-TeX-main-I,MJXc-TeX-main-Ix,MJXc-TeX-main-Iw} .MJXc-TeX-main-R {font-family: MJXc-TeX-main-R,MJXc-TeX-main-Rw} .MJXc-TeX-math-I {font-family: MJXc-TeX-math-I,MJXc-TeX-math-Ix,MJXc-TeX-math-Iw} .MJXc-TeX-size1-R {font-family: MJXc-TeX-size1-R,MJXc-TeX-size1-Rw} .MJXc-TeX-size2-R {font-family: MJXc-TeX-size2-R,MJXc-TeX-size2-Rw} .MJXc-TeX-size3-R {font-family: MJXc-TeX-size3-R,MJXc-TeX-size3-Rw} .MJXc-TeX-size4-R {font-family: MJXc-TeX-size4-R,MJXc-TeX-size4-Rw} @font-face {font-family: MJXc-TeX-ams-R; src: local('MathJax\_AMS'), local('MathJax\_AMS-Regular')} @font-face {font-family: MJXc-TeX-ams-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_AMS-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_AMS-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_AMS-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-cal-B; src: local('MathJax\_Caligraphic Bold'), local('MathJax\_Caligraphic-Bold')} @font-face {font-family: MJXc-TeX-cal-Bx; src: local('MathJax\_Caligraphic'); font-weight: bold} @font-face {font-family: MJXc-TeX-cal-Bw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Caligraphic-Bold.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Caligraphic-Bold.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Caligraphic-Bold.otf') format('opentype')} @font-face {font-family: MJXc-TeX-frak-R; src: local('MathJax\_Fraktur'), local('MathJax\_Fraktur-Regular')} @font-face {font-family: MJXc-TeX-frak-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Fraktur-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Fraktur-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Fraktur-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-frak-B; src: local('MathJax\_Fraktur Bold'), local('MathJax\_Fraktur-Bold')} @font-face {font-family: MJXc-TeX-frak-Bx; src: local('MathJax\_Fraktur'); font-weight: bold} @font-face {font-family: MJXc-TeX-frak-Bw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Fraktur-Bold.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Fraktur-Bold.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Fraktur-Bold.otf') format('opentype')} @font-face {font-family: MJXc-TeX-math-BI; src: local('MathJax\_Math BoldItalic'), local('MathJax\_Math-BoldItalic')} @font-face {font-family: MJXc-TeX-math-BIx; src: local('MathJax\_Math'); font-weight: bold; font-style: italic} @font-face {font-family: MJXc-TeX-math-BIw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Math-BoldItalic.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Math-BoldItalic.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Math-BoldItalic.otf') format('opentype')} @font-face {font-family: MJXc-TeX-sans-R; src: local('MathJax\_SansSerif'), local('MathJax\_SansSerif-Regular')} @font-face {font-family: MJXc-TeX-sans-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_SansSerif-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_SansSerif-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_SansSerif-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-sans-B; src: local('MathJax\_SansSerif Bold'), local('MathJax\_SansSerif-Bold')} @font-face {font-family: MJXc-TeX-sans-Bx; src: local('MathJax\_SansSerif'); font-weight: bold} @font-face {font-family: MJXc-TeX-sans-Bw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_SansSerif-Bold.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_SansSerif-Bold.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_SansSerif-Bold.otf') format('opentype')} @font-face {font-family: MJXc-TeX-sans-I; src: local('MathJax\_SansSerif Italic'), local('MathJax\_SansSerif-Italic')} @font-face {font-family: MJXc-TeX-sans-Ix; src: local('MathJax\_SansSerif'); font-style: italic} @font-face {font-family: MJXc-TeX-sans-Iw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_SansSerif-Italic.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_SansSerif-Italic.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_SansSerif-Italic.otf') format('opentype')} @font-face {font-family: MJXc-TeX-script-R; src: local('MathJax\_Script'), local('MathJax\_Script-Regular')} @font-face {font-family: MJXc-TeX-script-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Script-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Script-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Script-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-type-R; src: local('MathJax\_Typewriter'), local('MathJax\_Typewriter-Regular')} @font-face {font-family: MJXc-TeX-type-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Typewriter-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Typewriter-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Typewriter-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-cal-R; src: local('MathJax\_Caligraphic'), local('MathJax\_Caligraphic-Regular')} @font-face {font-family: MJXc-TeX-cal-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Caligraphic-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Caligraphic-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Caligraphic-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-main-B; src: local('MathJax\_Main Bold'), local('MathJax\_Main-Bold')} @font-face {font-family: MJXc-TeX-main-Bx; src: local('MathJax\_Main'); font-weight: bold} @font-face {font-family: MJXc-TeX-main-Bw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Main-Bold.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Main-Bold.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Main-Bold.otf') format('opentype')} @font-face {font-family: MJXc-TeX-main-I; src: local('MathJax\_Main Italic'), local('MathJax\_Main-Italic')} @font-face {font-family: MJXc-TeX-main-Ix; src: local('MathJax\_Main'); font-style: italic} @font-face {font-family: MJXc-TeX-main-Iw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Main-Italic.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Main-Italic.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Main-Italic.otf') format('opentype')} @font-face {font-family: MJXc-TeX-main-R; src: local('MathJax\_Main'), local('MathJax\_Main-Regular')} @font-face {font-family: MJXc-TeX-main-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Main-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Main-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Main-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-math-I; src: local('MathJax\_Math Italic'), local('MathJax\_Math-Italic')} @font-face {font-family: MJXc-TeX-math-Ix; src: local('MathJax\_Math'); font-style: italic} @font-face {font-family: MJXc-TeX-math-Iw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Math-Italic.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Math-Italic.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Math-Italic.otf') format('opentype')} @font-face {font-family: MJXc-TeX-size1-R; src: local('MathJax\_Size1'), local('MathJax\_Size1-Regular')} @font-face {font-family: MJXc-TeX-size1-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Size1-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Size1-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Size1-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-size2-R; src: local('MathJax\_Size2'), local('MathJax\_Size2-Regular')} @font-face {font-family: MJXc-TeX-size2-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Size2-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Size2-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Size2-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-size3-R; src: local('MathJax\_Size3'), local('MathJax\_Size3-Regular')} @font-face {font-family: MJXc-TeX-size3-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Size3-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Size3-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Size3-Regular.otf') format('opentype')} @font-face {font-family: MJXc-TeX-size4-R; src: local('MathJax\_Size4'), local('MathJax\_Size4-Regular')} @font-face {font-family: MJXc-TeX-size4-Rw; src /\*1\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/eot/MathJax\_Size4-Regular.eot'); src /\*2\*/: url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/woff/MathJax\_Size4-Regular.woff') format('woff'), url('https://yandex.st/contest/mathjax/fonts/HTML-CSS/TeX/otf/MathJax\_Size4-Regular.otf') format('opentype')}

[

Яндекс

](https://www.ya.ru/)[

Контест

](https://contest.yandex.ru/)

Русский

*   Русский
*   [
    
    English](http://contest.yandex.ru/contest/66792/problems/?lang=en)
*   [
    
    հայկ](http://contest.yandex.ru/contest/66792/problems/?lang=hy)
*   [
    
    Қазақша](http://contest.yandex.ru/contest/66792/problems/?lang=kk)
*   [
    
    O'zbek tili](http://contest.yandex.ru/contest/66792/problems/?lang=uz)

[Альберт Костански](https://passport.yandex.ru/passport?mode=passport)

*   [![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)99+ новых писем](https://mail.yandex.ru/)
    
*   [Написать письмо](https://mail.yandex.ru/compose)
    
*   [![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)Мой Диск](https://disk.yandex.ru/?source=main-loginmenu)
    

*   [Настройка](http://tune.yandex.ru/)
    
*   [Паспорт](https://passport.yandex.ru/)
    
*   [Выйти](https://passport.yandex.ru/passport?mode=logout&yu=323119361728280412&retpath=http%3A%2F%2Fcontest.yandex.ru%2Fcontest%2F66792%2Fproblems%2F)
    

*   [Пробный контест](https://contest.yandex.ru/contest/3/enter/)
*   [Архив соревнований](https://contest.yandex.ru/contest-list/)
*   [Настройки компиляторов](https://contest.yandex.ru/compilers/)
*   [Значения ошибок](https://contest.yandex.ru/errors/)
*   [Команды](https://contest.yandex.ru/teams/)

[Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование)](https://contest.yandex.ru/contest/66792/enter/?retPage=)

![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)

6 ноя 2024, 13:00:41

старт:

24 окт 2024, 19:00:00

финиш:

29 окт 2024, 18:00:00

длительность:

4д. 23ч.

начало:

24 окт 2024, 19:00:00

конец:

29 окт 2024, 18:00:00

...

Объявления жюри

![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)Ваше участие в соревновании завершено. Вы можете дорешивать задачи и отправлять решения вне соревнования

*   [Положение участников](https://contest.yandex.ru/contest/66792/standings/)
*   [Задачи](https://contest.yandex.ru/contest/66792/problems/)
*   [Посылки](https://contest.yandex.ru/contest/66792/submits/)

A. Плот
=======

Ограничение времени

1 секунда

Ограничение памяти

256Mb

Ввод

стандартный ввод или input.txt

Вывод

стандартный вывод или output.txt

Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты ( x1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> x </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x\_1 </annotation> </semantics> </math>x1​, y1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> y </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y\_1 </annotation> </semantics> </math>y1​), северо-восточный угол – координаты ( x2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> x </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x\_2 </annotation> </semantics> </math>x2​, y2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> y </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y\_2 </annotation> </semantics> </math>y2​).

Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.

![image](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/statement-file)

Формат ввода
------------

Программа получает на вход шесть чисел в следующем порядке: x1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> x </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x\_1 </annotation> </semantics> </math>x1​, y1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> y </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y\_1 </annotation> </semantics> </math>y1​ (координаты юго-западного угла плота), x2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> x </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x\_2 </annotation> </semantics> </math>x2​, y2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> y </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y\_2 </annotation> </semantics> </math>y2​ (координаты северо-восточного угла плота), x<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> x </mi> </mrow> <annotation encoding="application/x-tex"> x </annotation> </semantics> </math>x, y<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> y </mi> </mrow> <annotation encoding="application/x-tex"> y </annotation> </semantics> </math>y (координаты пловца). Все числа целые и по модулю не превосходят 100. Гарантируется, что x1<x2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> x </mi> <mn> 1 </mn> </msub> <mo> &lt; </mo> <msub> <mi> x </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x\_1 &lt; x\_2 </annotation> </semantics> </math>x1​<x2​, y1<y2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <msub> <mi> y </mi> <mn> 1 </mn> </msub> <mo> &lt; </mo> <msub> <mi> y </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y\_1 &lt; y\_2 </annotation> </semantics> </math>y1​<y2​, x≠x1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> x </mi> <mo mathvariant="normal"> ≠ </mo> <msub> <mi> x </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x \\ne x\_1 </annotation> </semantics> </math>x\=x1​, x≠x2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> x </mi> <mo mathvariant="normal"> ≠ </mo> <msub> <mi> x </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> x \\ne x\_2 </annotation> </semantics> </math>x\=x2​, y≠y1<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> y </mi> <mo mathvariant="normal"> ≠ </mo> <msub> <mi> y </mi> <mn> 1 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y \\ne y\_1 </annotation> </semantics> </math>y\=y1​, y≠y2<math xmlns="http://www.w3.org/1998/Math/MathML"> <semantics> <mrow> <mi> y </mi> <mo mathvariant="normal"> ≠ </mo> <msub> <mi> y </mi> <mn> 2 </mn> </msub> </mrow> <annotation encoding="application/x-tex"> y \\ne y\_2 </annotation> </semantics> </math>y\=y2​, координаты пловца находятся вне плота.

Формат вывода
-------------

Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”, к южной — символ ”S”, к западной — символ ”W”, к восточной — символ ”E”. Если пловцу следует плыть к углу плота, нужно вывести одну из следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.

Пример
------

Ввод

 ![Скопировать ввод](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)

Вывод

 ![Скопировать вывод](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)

\-1
-2
5
3
-4
6

NW

ЯзыкC++20 (GCC 14.1)C# (.NET 8.0)C++20 (GCC 14.1)Dart 3.5.1Go 1.23.0Haskell 7.10.2Java 22 (Temurin JDK)Kotlin 2.0.10 (JRE 21)Node.js 20.14.0PascalABC.NET 3.9.0PHP 8.1Python 3.12.3Python 3.9 (PyPy 7.3.16)Ruby 2.2.3Rust 1.80.1Scala 2.13.4Swift 5.10.1TypeScript 5.4.5

Набрать здесьОтправить файл

#include <iostream> int main(){ int x1, y1, x2, y2, x, y; std::cin >> x1 >> y1 >> x2 >> y2 >> x >> y; if (x1 <= x && x <= x2){ std::cout << (std::abs(y - y1) < std::abs(y - y2)? "S" : "N"); return 0; } if (y1 <= y && y <= y2){ std::cout << (std::abs(x - x1) < std::abs(x - x2)? "W" : "E"); return 0; } if (x < x1){ std::cout << (y < y1 ? "SW" : "NW"); return 0; } std::cout << (y < y1 ? "SE" : "NE"); return 0; }

x

1

#include <iostream>

2

​

3

int main(){

4

    int x1, y1, x2, y2, x, y;

5

    std::cin \>> x1 \>> y1 \>> x2 \>> y2 \>> x \>> y;

6

    if (x1 <= x && x <= x2){

7

        std::cout << (std::abs(y \- y1) < std::abs(y \- y2)? "S" : "N");

8

        return 0;

9

    }

10

    if (y1 <= y && y <= y2){

11

        std::cout << (std::abs(x \- x1) < std::abs(x \- x2)? "W" : "E");

12

        return 0;

13

    }

14

    if (x < x1){

15

    std::cout << (y < y1 ? "SW" : "NW");

16

    return 0;

17

}

18

    std::cout << (y < y1 ? "SE" : "NE");

19

    return 0;

20

}

21

​

Выбрать![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)Файл не выбран![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)

Отправить

![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)![](./A. Плот — Тренировки по алгоритмам 6.0 от Яндекса — Занятие 1 (Тестирование) — Яндекс.Контест_files/La6qi18Z8LwgnZdsAr1qy1GwCwo.gif)осталось 100 попыток

[Следующая](https://contest.yandex.ru/contest/66792/problems/B/)

*   [A. Плот](https://contest.yandex.ru/contest/66792/problems/A/)
    
    [](https://contest.yandex.ru/contest/66792/problems/A/)[](https://contest.yandex.ru/contest/66792/run-report/122399397/)
    
*   [B. Майки и носки](https://contest.yandex.ru/contest/66792/problems/B/)
    
    [](https://contest.yandex.ru/contest/66792/problems/B/)[](https://contest.yandex.ru/contest/66792/run-report/122754612/)
    
*   [C. Надпись на табло](https://contest.yandex.ru/contest/66792/problems/C/)
    
    [](https://contest.yandex.ru/contest/66792/problems/C/)[](https://contest.yandex.ru/contest/66792/run-report/122819647/)
    
*   [D. Кондиционер (составление тестов)](https://contest.yandex.ru/contest/66792/problems/D/)
    
    [](https://contest.yandex.ru/contest/66792/problems/D/)[](https://contest.yandex.ru/contest/66792/run-report/122880917/)
    
*   [E. Наибольшее произведение двух чисел (составление тестов)](https://contest.yandex.ru/contest/66792/problems/E/)
    
    [](https://contest.yandex.ru/contest/66792/problems/E/)[](https://contest.yandex.ru/contest/66792/run-report/122906935/)
    

Время посылки

ID

Задача

Компилятор

Вердикт

Тип посылки

Время

Память

Тест

Баллы

28 окт 2024, 23:27:28

122883280

A

C++20 (GCC 14.1)

[OK](https://contest.yandex.ru/contest/66792/run-report/122883280/)

\-

2ms

2.13Mb

\-

\-

[отчёт](https://contest.yandex.ru/contest/66792/run-report/122883280/)

28 окт 2024, 23:24:33

122882978

A

C++20 (GCC 14.1)

[WA](https://contest.yandex.ru/contest/66792/run-report/122882978/)

\-

2ms

2.00Mb

1

\-

[отчёт](https://contest.yandex.ru/contest/66792/run-report/122882978/)

28 окт 2024, 23:20:50

122882623

A

C++20 (GCC 14.1)

[WA](https://contest.yandex.ru/contest/66792/run-report/122882623/)

\-

2ms

2.00Mb

3

\-

[отчёт](https://contest.yandex.ru/contest/66792/run-report/122882623/)

28 окт 2024, 23:15:34

122882140

A

C++20 (GCC 14.1)

[WA](https://contest.yandex.ru/contest/66792/run-report/122882140/)

\-

2ms

2.00Mb

3

\-

[отчёт](https://contest.yandex.ru/contest/66792/run-report/122882140/)

25 окт 2024, 10:11:08

122399397

A

Python 3.12.3

[OK](https://contest.yandex.ru/contest/66792/run-report/122399397/)

\-

35ms

4.38Mb

\-

\-

[отчёт](https://contest.yandex.ru/contest/66792/run-report/122399397/)

[Справка](https://yandex.ru/support/contest/index.html)[Обратная связь](https://yandex.ru/support/contest/troubleshooting.xml?form1580-cntst_link=http%3A%2F%2Fcontest.yandex.ru%2Fcontest%2F66792%2Fproblems%2F&form1580-cntst_login=%D0%90%D0%BB%D1%8C%D0%B1%D0%B5%D1%80%D1%82%20%D0%9A%D0%BE%D1%81%D1%82%D0%B0%D0%BD%D1%81%D0%BA%D0%B8)[Пользовательское соглашение](https://yandex.ru/legal/contest_termsofuse/)

© 2013–2024  ООО «[Яндекс](http://www.ya.ru/)»

__

![](//mc.yandex.ru/watch/16150693)

__Ya.Feedback.App.embed(document.body); Ya.Feedback.App.init("4d064ba8-48b0-4ff6-8342-5c77558dc135", {from: 'old-contest'}); Ya.Feedback.App.fetch();