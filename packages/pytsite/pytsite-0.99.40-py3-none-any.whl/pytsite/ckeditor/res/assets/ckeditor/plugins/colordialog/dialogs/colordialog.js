﻿/*
 Copyright (c) 2003-2015, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or http://ckeditor.com/license
*/
CKEDITOR.dialog.add("colordialog",function(x){function q(){d.getById(r).removeStyle("background-color");t.getContentElement("picker","selectedColor").setValue("");l&&l.removeAttribute("aria-selected");l=null}function y(a){a=a.data.getTarget();var c;"td"==a.getName()&&(c=a.getChild(0).getHtml())&&(l=a,l.setAttribute("aria-selected",!0),t.getContentElement("picker","selectedColor").setValue(c))}function C(a){a=a.replace(/^#/,"");for(var c=0,b=[];2>=c;c++)b[c]=parseInt(a.substr(2*c,2),16);return"#"+
(165<=.2126*b[0]+.7152*b[1]+.0722*b[2]?"000":"fff")}function z(a){!a.name&&(a=new CKEDITOR.event(a));var c=!/mouse/.test(a.name),b=a.data.getTarget(),g;"td"==b.getName()&&(g=b.getChild(0).getHtml())&&(u(a),c?e=b:A=b,c&&(b.setStyle("border-color",C(g)),b.setStyle("border-style","dotted")),d.getById(m).setStyle("background-color",g),d.getById(n).setHtml(g))}function u(a){if(a=!/mouse/.test(a.name)&&e){var c=a.getChild(0).getHtml();a.setStyle("border-color",c);a.setStyle("border-style","solid")}e||A||
(d.getById(m).removeStyle("background-color"),d.getById(n).setHtml("\x26nbsp;"))}function D(a){var c=a.data,b=c.getTarget(),g=c.getKeystroke(),d="rtl"==x.lang.dir;switch(g){case 38:if(a=b.getParent().getPrevious())a=a.getChild([b.getIndex()]),a.focus();c.preventDefault();break;case 40:(a=b.getParent().getNext())&&(a=a.getChild([b.getIndex()]))&&1==a.type&&a.focus();c.preventDefault();break;case 32:case 13:y(a);c.preventDefault();break;case d?37:39:(a=b.getNext())?1==a.type&&(a.focus(),c.preventDefault(!0)):
(a=b.getParent().getNext())&&(a=a.getChild([0]))&&1==a.type&&(a.focus(),c.preventDefault(!0));break;case d?39:37:if(a=b.getPrevious())a.focus(),c.preventDefault(!0);else if(a=b.getParent().getPrevious())a=a.getLast(),a.focus(),c.preventDefault(!0)}}var v=CKEDITOR.dom.element,d=CKEDITOR.document,f=x.lang.colordialog,t,B={type:"html",html:"\x26nbsp;"},l,e,A,p=function(a){return CKEDITOR.tools.getNextId()+"_"+a},m=p("hicolor"),n=p("hicolortext"),r=p("selhicolor"),h;(function(){function a(a,d){for(var w=
a;w<a+3;w++){var e=new v(h.$.insertRow(-1));e.setAttribute("role","row");for(var f=d;f<d+3;f++)for(var g=0;6>g;g++)c(e.$,"#"+b[f]+b[g]+b[w])}}function c(a,c){var b=new v(a.insertCell(-1));b.setAttribute("class","ColorCell");b.setAttribute("tabIndex",-1);b.setAttribute("role","gridcell");b.on("keydown",D);b.on("click",y);b.on("focus",z);b.on("blur",u);b.setStyle("background-color",c);b.setStyle("border","1px solid "+c);b.setStyle("width","14px");b.setStyle("height","14px");var d=p("color_table_cell");
b.setAttribute("aria-labelledby",d);b.append(CKEDITOR.dom.element.createFromHtml('\x3cspan id\x3d"'+d+'" class\x3d"cke_voice_label"\x3e'+c+"\x3c/span\x3e",CKEDITOR.document))}h=CKEDITOR.dom.element.createFromHtml('\x3ctable tabIndex\x3d"-1" aria-label\x3d"'+f.options+'" role\x3d"grid" style\x3d"border-collapse:separate;" cellspacing\x3d"0"\x3e\x3ccaption class\x3d"cke_voice_label"\x3e'+f.options+'\x3c/caption\x3e\x3ctbody role\x3d"presentation"\x3e\x3c/tbody\x3e\x3c/table\x3e');h.on("mouseover",z);
h.on("mouseout",u);var b="00 33 66 99 cc ff".split(" ");a(0,0);a(3,0);a(0,3);a(3,3);var d=new v(h.$.insertRow(-1));d.setAttribute("role","row");c(d.$,"#000000");for(var e=0;16>e;e++){var k=e.toString(16);c(d.$,"#"+k+k+k+k+k+k)}c(d.$,"#ffffff")})();return{title:f.title,minWidth:360,minHeight:220,onLoad:function(){t=this},onHide:function(){q();var a=e.getChild(0).getHtml();e.setStyle("border-color",a);e.setStyle("border-style","solid");d.getById(m).removeStyle("background-color");d.getById(n).setHtml("\x26nbsp;");
e=null},contents:[{id:"picker",label:f.title,accessKey:"I",elements:[{type:"hbox",padding:0,widths:["70%","10%","30%"],children:[{type:"html",html:"\x3cdiv\x3e\x3c/div\x3e",onLoad:function(){CKEDITOR.document.getById(this.domId).append(h)},focus:function(){(e||this.getElement().getElementsByTag("td").getItem(0)).focus()}},B,{type:"vbox",padding:0,widths:["70%","5%","25%"],children:[{type:"html",html:"\x3cspan\x3e"+f.highlight+'\x3c/span\x3e\x3cdiv id\x3d"'+m+'" style\x3d"border: 1px solid; height: 74px; width: 74px;"\x3e\x3c/div\x3e\x3cdiv id\x3d"'+
n+'"\x3e\x26nbsp;\x3c/div\x3e\x3cspan\x3e'+f.selected+'\x3c/span\x3e\x3cdiv id\x3d"'+r+'" style\x3d"border: 1px solid; height: 20px; width: 74px;"\x3e\x3c/div\x3e'},{type:"text",label:f.selected,labelStyle:"display:none",id:"selectedColor",style:"width: 76px;margin-top:4px",onChange:function(){try{d.getById(r).setStyle("background-color",this.getValue())}catch(a){q()}}},B,{type:"button",id:"clear",label:f.clear,onClick:q}]}]}]}]}});