if(!RedactorPlugins)var RedactorPlugins={};RedactorPlugins.bufferbuttons=function()
{return{init:function()
{var undo=this.button.addFirst('undo','Rückgängig');var redo=this.button.addAfter('undo','redo','Wiederherstellen');this.button.addCallback(undo,this.buffer.undo);this.button.addCallback(redo,this.buffer.redo);}};};(function($)
{$.Redactor.prototype.definedlinks=function()
{return{init:function()
{if(!this.opts.definedLinks)return;this.modal.addCallback('link',$.proxy(this.definedlinks.load,this));},load:function()
{var $select=$('<select id="redactor-defined-links" />');$('#redactor-modal-link-insert').prepend($select);this.definedlinks.storage={};$.getJSON(this.opts.definedLinks,$.proxy(function(data)
{var grouped=_.groupBy(data,function(d){return d.group;});var key=0;$.each(_.groupBy(data,'group'),$.proxy(function(group,links){var $optgroup=$('<optgroup />').attr('label',group);$select.append($optgroup);$.each(links,$.proxy(function(ix,val){this.definedlinks.storage[key]=val;$optgroup.append($('<option>').val(key).html(val.name));key+=1;},this));},this));$select.prop('selectedIndex',-1);$select.on('change',$.proxy(this.definedlinks.select,this));},this));},select:function(e)
{var key=$(e.target).val();var name='',url='';if(key!==0)
{name=this.definedlinks.storage[key].name;url=this.definedlinks.storage[key].url;}
$('#redactor-link-url').val(url);$('#redactor-link-url-text').val(name);}};};})(jQuery);(function($)
{$.Redactor.prototype.filemanager=function()
{return{init:function()
{if(!this.opts.fileManagerJson)return;this.modal.addCallback('file',this.filemanager.load);},load:function()
{var $modal=this.modal.getModal();this.modal.createTabber($modal);this.modal.addTab(1,'Hochladen','active');this.modal.addTab(2,'Auswählen');$('#redactor-modal-file-upload-box').addClass('redactor-tab redactor-tab1');var $box=$('<div id="redactor-file-manager-box" class="redactor-tab redactor-tab2">').hide();$modal.append($box);$.ajax({dataType:"json",cache:false,url:this.opts.fileManagerJson,success:$.proxy(function(data)
{var ul=$('<ul id="redactor-modal-list">');$.each(data,$.proxy(function(key,val)
{var a=$('<a href="#" title="'+val.title+'" rel="'+val.link+'" class="redactor-file-manager-link">'+val.title+'</a>');var li=$('<li />');a.on('click',$.proxy(this.filemanager.insert,this));li.append(a);ul.append(li);},this));$('#redactor-file-manager-box').append(ul);},this)});},insert:function(e)
{e.preventDefault();var $target=$(e.target).closest('.redactor-file-manager-link');this.file.insert('<a href="'+$target.attr('rel')+'">'+$target.attr('title')+'</a>');}};};})(jQuery);if(!RedactorPlugins)var RedactorPlugins={};(function($)
{RedactorPlugins.imagemanager=function()
{return{init:function()
{if(!this.opts.imageManagerJson)return;this.modal.addCallback('image',this.imagemanager.load);},load:function()
{var $modal=this.modal.getModal();this.modal.createTabber($modal);this.modal.addTab(1,'Hochladen','active');this.modal.addTab(2,'Auswählen');$('#redactor-modal-image-droparea').addClass('redactor-tab redactor-tab1');var $box=$('<div id="redactor-image-manager-box" style="overflow: auto; height: 300px;" class="redactor-tab redactor-tab2">').hide();$modal.append($box);$.ajax({dataType:"json",cache:false,url:this.opts.imageManagerJson,success:$.proxy(function(data)
{$.each(data,$.proxy(function(key,groups)
{var group=$('<p style="margin: 1rem 0 0 0;">'+groups.group+'</p>');$('#redactor-image-manager-box').append(group);$.each(groups.images,$.proxy(function(key,val)
{var thumbtitle='';if(typeof val.title!=='undefined')thumbtitle=val.title;var img=$('<img class="lazyload" data-src="'+val.thumb+'" rel="'+val.image+'" title="'+thumbtitle+'" style="max-width: 192px; max-height: 192px; cursor: pointer;" />');$('#redactor-image-manager-box').append(img);$(img).click($.proxy(this.imagemanager.insert,this));},this));},this));this.observe.images();},this)});},insert:function(e)
{var url=$(e.target).attr('rel');this.image.insert('<img src="'+url+'">');}};};})(jQuery);(function($){$.Redactor.opts.langs['de']={html:'HTML',video:'Video',image:'Bilder',table:'Tabelle',link:'Link',link_insert:'Link einfügen ...',link_edit:'Link bearbeiten',unlink:'Link entfernen',formatting:'Formatvorlagen',paragraph:'Absatz',quote:'Zitat',code:'Code',header1:'Überschrift 1',header2:'Überschrift 2',header3:'Überschrift 3',header4:'Überschrift 4',header5:'Überschrift 5',bold:'Fett',italic:'Kursiv',fontcolor:'Schriftfarbe',backcolor:'Texthervorhebungsfarbe',unorderedlist:'Aufzählungszeichen',orderedlist:'Nummerierung',outdent:'Einzug verkleinern',indent:'Einzug vergrößern',redo:'Wiederholen',undo:'Rückgängig',cut:'Ausschneiden',cancel:'Abbrechen',insert:'Einfügen',save:'Speichern',_delete:'Löschen',insert_table:'Tabelle einfügen',insert_row_above:'Zeile oberhalb einfügen',insert_row_below:'Zeile unterhalb einfügen',insert_column_left:'Spalte links einfügen',insert_column_right:'Spalte rechts einfügen',delete_column:'Spalte löschen',delete_row:'Zeile löschen',delete_table:'Tabelle löschen',rows:'Zeilen',columns:'Spalten',add_head:'Titel einfügen',delete_head:'Titel entfernen',title:'Title',image_view:'Bilder',image_position:'Textumbruch',none:'Keine',left:'Links',right:'Rechts',image_web_link:'Bilder-Link',text:'Text',mailto:'Email',web:'URL',video_html_code:'Video-Einbettungscode',file:'Datei',upload:'Hochladen',download:'Download',choose:'Auswählen',or_choose:'Oder, wählen Sie eine Datei aus',drop_file_here:'Ziehen Sie eine Datei hier hin',align_left:'Linksbündig',align_center:'Mitte',align_right:'Rechtsbündig',align_justify:'Blocksatz',horizontalrule:'Horizontale Linie',fullscreen:'Vollbild',deleted:'Durchgestrichen',anchor:'Anker',link_new_tab:'Link in neuem Tab öffnen',underline:'Unterstrichen',alignment:'Ausrichtung',filename:'Name (optional)',edit:'Bearbeiten',center:'Center',upload_label:'Datei hier ablegen oder '};})(jQuery);function handleUploadError(json){show_confirmation(json.message,undefined,"Ok");}
var setup_internal_link_select=function(input){input=$(input);var types=get_types(input);var button=get_button_face(types);if(types.length===0){return;}
input.wrap('<div class="small-11 columns"></div>');input.closest('.columns').wrap('<div class="row collapse input-with-button">');input.closest('.row').append('<div class="small-1 columns"><a class="button secondary postfix">'+button+'</a></div>');var row=input.closest('.row');for(var i=0;i<types.length;i++){row.addClass(types[i]);}
if(types.length==1){row.find('.button').click(function(e){on_internal_link_button_click(input,types[0]);e.preventDefault();return false;});}else{row.find('.button').click(function(e){var popup_content=$('<div class="popup" />');if(types.indexOf('image-url')!=-1){popup_content.append($('<a class="image-url">Bild</a>'));}
if(types.indexOf('file-url')!=-1){popup_content.append($('<a class="file-url">Datei</a>'));}
if(types.indexOf('internal-url')!=-1){popup_content.append($('<a class="internal-url">Interner Link</a>'));}
popup_content.popup({'autoopen':true,'horizontal':'right','offsetleft':8,'tooltipanchor':row.find('.button'),'transition':null,'type':'tooltip','onopen':function(){var popup=$(this);popup.find('a').click(function(){popup.popup('hide');});popup.find('a').click(function(e){var type=get_types($(this))[0];on_internal_link_button_click(input,type);e.preventDefault();});},'detach':true});e.preventDefault();return false;});}};var get_types=function(input){var types=[];if($(input).hasClass('image-url')){types.push('image-url');}
if($(input).hasClass('file-url')){types.push('file-url');}
if($(input).hasClass('internal-url')){types.push('internal-url');}
return types;};var get_button_face=function(types){if(types.length==1){if(types[0]=='image-url'){return'<i class="fa fa-picture-o"></i>';}
if(types[0]=='file-url'){return'<i class="fa fa-paperclip"></i>';}
if(types[0]=='internal-url'){return'<i class="fa fa-link"></i>';}}
return'…';};var on_internal_link_button_click=function(input,type){var form=$(input).closest('form');var virtual=$('<textarea><p></p></textarea>').redactor({plugins:['imagemanager','filemanager','definedlinks'],fileUpload:form.data('file-upload-url'),fileManagerJson:form.data('file-list-url'),imageUpload:form.data('image-upload-url'),imageManagerJson:form.data('image-list-url'),definedLinks:form.data('sitecollection-url'),lang:'de',fileUploadErrorCallback:handleUploadError,imageUploadErrorCallback:handleUploadError});var redactor=virtual.data('redactor');redactor.insert.html=jQuery.proxy(function(html){var input=$(this);input.val($(html).attr('src')||$(html).attr('href'));},input);redactor.$textarea.on('insertedLinkCallback.redactor',jQuery.proxy(function(args){var input=$(this[0]);var redactor=this[1];input.val($(redactor.modal.getModal()).find('input[type="url"]').val());},[input,redactor]));redactor.$textarea.on('modalOpenedCallback.redactor',function(){this.$modal.addClass('input-with-button');});redactor.$textarea.on('modalClosedCallback.redactor',function(){this.core.destroy();});redactor.selection.addRange=function(){};redactor.selection.getCurrent=function(){return $(virtual).find('p');};var mapping={'image-url':'image.show','file-url':'file.show','internal-url':'link.show'};$(virtual).redactor(mapping[type]);};jQuery.fn.internal_link_select=function(){return this.each(function(){setup_internal_link_select(this);});};$(document).ready(function(){$('.image-url, .file-url, .internal-url').internal_link_select();});$(function(){_.each($('textarea.editor'),function(el){var textarea=$(el);var form=textarea.closest('form');textarea.redactor({buttons:['formatting','bold','italic','deleted','unorderedlist','orderedlist','image','file','link','horizontalrule','html'],formatting:['p','blockquote'],fileUpload:form.data('file-upload-url'),fileManagerJson:form.data('file-list-url'),imageUpload:form.data('image-upload-url'),imageManagerJson:form.data('image-list-url'),definedLinks:form.data('sitecollection-url'),plugins:['bufferbuttons','filemanager','imagemanager','definedlinks'],lang:'de',convertVideoLinks:false,formattingAdd:[{tag:'h2',title:"Titel"},{tag:'h3',title:"Untertitel"}],fileUploadErrorCallback:handleUploadError,imageUploadErrorCallback:handleUploadError});});});