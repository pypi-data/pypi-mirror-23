// Compiled by ClojureScript 1.9.229 {:static-fns true, :optimize-constants true}
goog.provide('cljs_http.core');
goog.require('cljs.core');
goog.require('goog.net.ErrorCode');
goog.require('goog.net.EventType');
goog.require('cljs.core.async');
goog.require('cljs_http.util');
goog.require('goog.net.Jsonp');
goog.require('clojure.string');
goog.require('goog.net.XhrIo');
cljs_http.core.pending_requests = (function (){var G__71118 = cljs.core.PersistentArrayMap.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__71118) : cljs.core.atom.call(null,G__71118));
})();
/**
 * Attempt to close the given channel and abort the pending HTTP request
 *   with which it is associated.
 */
cljs_http.core.abort_BANG_ = (function cljs_http$core$abort_BANG_(channel){
var temp__6728__auto__ = (cljs.core.deref.cljs$core$IFn$_invoke$arity$1 ? cljs.core.deref.cljs$core$IFn$_invoke$arity$1(cljs_http.core.pending_requests) : cljs.core.deref.call(null,cljs_http.core.pending_requests)).call(null,channel);
if(cljs.core.truth_(temp__6728__auto__)){
var req = temp__6728__auto__;
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(cljs_http.core.pending_requests,cljs.core.dissoc,channel);

cljs.core.async.close_BANG_(channel);

if(cljs.core.truth_(req.hasOwnProperty("abort"))){
return req.abort();
} else {
return cljs.core.cst$kw$jsonp.cljs$core$IFn$_invoke$arity$1(req).cancel(cljs.core.cst$kw$request.cljs$core$IFn$_invoke$arity$1(req));
}
} else {
return null;
}
});
cljs_http.core.aborted_QMARK_ = (function cljs_http$core$aborted_QMARK_(xhr){
return cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(xhr.getLastErrorCode(),goog.net.ErrorCode.ABORT);
});
/**
 * Takes an XhrIo object and applies the default-headers to it.
 */
cljs_http.core.apply_default_headers_BANG_ = (function cljs_http$core$apply_default_headers_BANG_(xhr,headers){
var formatted_h = cljs.core.zipmap(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs_http.util.camelize,cljs.core.keys(headers)),cljs.core.vals(headers));
return cljs.core.dorun.cljs$core$IFn$_invoke$arity$1(cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (formatted_h){
return (function (p__71123){
var vec__71124 = p__71123;
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71124,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__71124,(1),null);
return xhr.headers.set(k,v);
});})(formatted_h))
,formatted_h));
});
/**
 * Takes an XhrIo object and sets response-type if not nil.
 */
cljs_http.core.apply_response_type_BANG_ = (function cljs_http$core$apply_response_type_BANG_(xhr,response_type){
return xhr.setResponseType((function (){var G__71128 = response_type;
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$array_DASH_buffer,G__71128)){
return goog.net.XhrIo.ResponseType.ARRAY_BUFFER;
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$blob,G__71128)){
return goog.net.XhrIo.ResponseType.BLOB;
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$document,G__71128)){
return goog.net.XhrIo.ResponseType.DOCUMENT;
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$text,G__71128)){
return goog.net.XhrIo.ResponseType.TEXT;
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$default,G__71128)){
return goog.net.XhrIo.ResponseType.DEFAULT;
} else {
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(null,G__71128)){
return goog.net.XhrIo.ResponseType.DEFAULT;
} else {
throw (new Error([cljs.core.str("No matching clause: "),cljs.core.str(response_type)].join('')));

}
}
}
}
}
}
})());
});
/**
 * Builds an XhrIo object from the request parameters.
 */
cljs_http.core.build_xhr = (function cljs_http$core$build_xhr(p__71129){
var map__71133 = p__71129;
var map__71133__$1 = ((((!((map__71133 == null)))?((((map__71133.cljs$lang$protocol_mask$partition0$ & (64))) || (map__71133.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__71133):map__71133);
var request = map__71133__$1;
var with_credentials_QMARK_ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71133__$1,cljs.core.cst$kw$with_DASH_credentials_QMARK_);
var default_headers = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71133__$1,cljs.core.cst$kw$default_DASH_headers);
var response_type = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71133__$1,cljs.core.cst$kw$response_DASH_type);
var timeout = (function (){var or__9278__auto__ = cljs.core.cst$kw$timeout.cljs$core$IFn$_invoke$arity$1(request);
if(cljs.core.truth_(or__9278__auto__)){
return or__9278__auto__;
} else {
return (0);
}
})();
var send_credentials = (((with_credentials_QMARK_ == null))?true:with_credentials_QMARK_);
var G__71135 = (new goog.net.XhrIo());
cljs_http.core.apply_default_headers_BANG_(G__71135,default_headers);

cljs_http.core.apply_response_type_BANG_(G__71135,response_type);

G__71135.setTimeoutInterval(timeout);

G__71135.setWithCredentials(send_credentials);

return G__71135;
});
cljs_http.core.error_kw = cljs.core.PersistentHashMap.fromArrays([(0),(7),(1),(4),(6),(3),(2),(9),(5),(8)],[cljs.core.cst$kw$no_DASH_error,cljs.core.cst$kw$abort,cljs.core.cst$kw$access_DASH_denied,cljs.core.cst$kw$custom_DASH_error,cljs.core.cst$kw$http_DASH_error,cljs.core.cst$kw$ff_DASH_silent_DASH_error,cljs.core.cst$kw$file_DASH_not_DASH_found,cljs.core.cst$kw$offline,cljs.core.cst$kw$exception,cljs.core.cst$kw$timeout]);
/**
 * Execute the HTTP request corresponding to the given Ring request
 *   map and return a core.async channel.
 */
cljs_http.core.xhr = (function cljs_http$core$xhr(p__71136){
var map__71165 = p__71136;
var map__71165__$1 = ((((!((map__71165 == null)))?((((map__71165.cljs$lang$protocol_mask$partition0$ & (64))) || (map__71165.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__71165):map__71165);
var request = map__71165__$1;
var request_method = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$request_DASH_method);
var headers = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$headers);
var body = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$body);
var with_credentials_QMARK_ = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$with_DASH_credentials_QMARK_);
var cancel = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$cancel);
var progress = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71165__$1,cljs.core.cst$kw$progress);
var channel = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var request_url = cljs_http.util.build_url(request);
var method = cljs.core.name((function (){var or__9278__auto__ = request_method;
if(cljs.core.truth_(or__9278__auto__)){
return or__9278__auto__;
} else {
return cljs.core.cst$kw$get;
}
})());
var headers__$1 = cljs_http.util.build_headers(headers);
var xhr__$1 = cljs_http.core.build_xhr(request);
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(cljs_http.core.pending_requests,cljs.core.assoc,channel,xhr__$1);

xhr__$1.listen(goog.net.EventType.COMPLETE,((function (channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress){
return (function (evt){
var target = evt.target;
var response = new cljs.core.PersistentArrayMap(null, 7, [cljs.core.cst$kw$status,target.getStatus(),cljs.core.cst$kw$success,target.isSuccess(),cljs.core.cst$kw$body,target.getResponse(),cljs.core.cst$kw$headers,cljs_http.util.parse_headers(target.getAllResponseHeaders()),cljs.core.cst$kw$trace_DASH_redirects,new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [request_url,target.getLastUri()], null),cljs.core.cst$kw$error_DASH_code,(function (){var G__71167 = target.getLastErrorCode();
return (cljs_http.core.error_kw.cljs$core$IFn$_invoke$arity$1 ? cljs_http.core.error_kw.cljs$core$IFn$_invoke$arity$1(G__71167) : cljs_http.core.error_kw.call(null,G__71167));
})(),cljs.core.cst$kw$error_DASH_text,target.getLastError()], null);
if(cljs.core.not(cljs_http.core.aborted_QMARK_(xhr__$1))){
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(channel,response);
} else {
}

cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(cljs_http.core.pending_requests,cljs.core.dissoc,channel);

if(cljs.core.truth_(cancel)){
cljs.core.async.close_BANG_(cancel);
} else {
}

return cljs.core.async.close_BANG_(channel);
});})(channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress))
);

if(cljs.core.truth_(progress)){
var listener_71193 = ((function (channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress){
return (function (direction,evt){
return cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(progress,cljs.core.merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$direction,direction,cljs.core.cst$kw$loaded,evt.loaded], null),(cljs.core.truth_(evt.lengthComputable)?new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$total,evt.total], null):null)], 0)));
});})(channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress))
;
var G__71168_71194 = xhr__$1;
G__71168_71194.setProgressEventsEnabled(true);

G__71168_71194.listen(goog.net.EventType.UPLOAD_PROGRESS,cljs.core.partial.cljs$core$IFn$_invoke$arity$2(listener_71193,cljs.core.cst$kw$upload));

G__71168_71194.listen(goog.net.EventType.DOWNLOAD_PROGRESS,cljs.core.partial.cljs$core$IFn$_invoke$arity$2(listener_71193,cljs.core.cst$kw$download));

} else {
}

xhr__$1.send(request_url,method,body,headers__$1);

if(cljs.core.truth_(cancel)){
var c__42110__auto___71195 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress){
return (function (){
var f__42111__auto__ = (function (){var switch__41984__auto__ = ((function (c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress){
return (function (state_71179){
var state_val_71180 = (state_71179[(1)]);
if((state_val_71180 === (1))){
var state_71179__$1 = state_71179;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_71179__$1,(2),cancel);
} else {
if((state_val_71180 === (2))){
var inst_71170 = (state_71179[(2)]);
var inst_71171 = xhr__$1.isComplete();
var inst_71172 = cljs.core.not(inst_71171);
var state_71179__$1 = (function (){var statearr_71181 = state_71179;
(statearr_71181[(7)] = inst_71170);

return statearr_71181;
})();
if(inst_71172){
var statearr_71182_71196 = state_71179__$1;
(statearr_71182_71196[(1)] = (3));

} else {
var statearr_71183_71197 = state_71179__$1;
(statearr_71183_71197[(1)] = (4));

}

return cljs.core.cst$kw$recur;
} else {
if((state_val_71180 === (3))){
var inst_71174 = xhr__$1.abort();
var state_71179__$1 = state_71179;
var statearr_71184_71198 = state_71179__$1;
(statearr_71184_71198[(2)] = inst_71174);

(statearr_71184_71198[(1)] = (5));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71180 === (4))){
var state_71179__$1 = state_71179;
var statearr_71185_71199 = state_71179__$1;
(statearr_71185_71199[(2)] = null);

(statearr_71185_71199[(1)] = (5));


return cljs.core.cst$kw$recur;
} else {
if((state_val_71180 === (5))){
var inst_71177 = (state_71179[(2)]);
var state_71179__$1 = state_71179;
return cljs.core.async.impl.ioc_helpers.return_chan(state_71179__$1,inst_71177);
} else {
return null;
}
}
}
}
}
});})(c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress))
;
return ((function (switch__41984__auto__,c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress){
return (function() {
var cljs_http$core$xhr_$_state_machine__41985__auto__ = null;
var cljs_http$core$xhr_$_state_machine__41985__auto____0 = (function (){
var statearr_71189 = [null,null,null,null,null,null,null,null];
(statearr_71189[(0)] = cljs_http$core$xhr_$_state_machine__41985__auto__);

(statearr_71189[(1)] = (1));

return statearr_71189;
});
var cljs_http$core$xhr_$_state_machine__41985__auto____1 = (function (state_71179){
while(true){
var ret_value__41986__auto__ = (function (){try{while(true){
var result__41987__auto__ = switch__41984__auto__(state_71179);
if(cljs.core.keyword_identical_QMARK_(result__41987__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__41987__auto__;
}
break;
}
}catch (e71190){if((e71190 instanceof Object)){
var ex__41988__auto__ = e71190;
var statearr_71191_71200 = state_71179;
(statearr_71191_71200[(5)] = ex__41988__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_71179);

return cljs.core.cst$kw$recur;
} else {
throw e71190;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__41986__auto__,cljs.core.cst$kw$recur)){
var G__71201 = state_71179;
state_71179 = G__71201;
continue;
} else {
return ret_value__41986__auto__;
}
break;
}
});
cljs_http$core$xhr_$_state_machine__41985__auto__ = function(state_71179){
switch(arguments.length){
case 0:
return cljs_http$core$xhr_$_state_machine__41985__auto____0.call(this);
case 1:
return cljs_http$core$xhr_$_state_machine__41985__auto____1.call(this,state_71179);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs_http$core$xhr_$_state_machine__41985__auto__.cljs$core$IFn$_invoke$arity$0 = cljs_http$core$xhr_$_state_machine__41985__auto____0;
cljs_http$core$xhr_$_state_machine__41985__auto__.cljs$core$IFn$_invoke$arity$1 = cljs_http$core$xhr_$_state_machine__41985__auto____1;
return cljs_http$core$xhr_$_state_machine__41985__auto__;
})()
;})(switch__41984__auto__,c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress))
})();
var state__42112__auto__ = (function (){var statearr_71192 = (f__42111__auto__.cljs$core$IFn$_invoke$arity$0 ? f__42111__auto__.cljs$core$IFn$_invoke$arity$0() : f__42111__auto__.call(null));
(statearr_71192[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__42110__auto___71195);

return statearr_71192;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__42112__auto__);
});})(c__42110__auto___71195,channel,request_url,method,headers__$1,xhr__$1,map__71165,map__71165__$1,request,request_method,headers,body,with_credentials_QMARK_,cancel,progress))
);

} else {
}

return channel;
});
/**
 * Execute the JSONP request corresponding to the given Ring request
 *   map and return a core.async channel.
 */
cljs_http.core.jsonp = (function cljs_http$core$jsonp(p__71202){
var map__71219 = p__71202;
var map__71219__$1 = ((((!((map__71219 == null)))?((((map__71219.cljs$lang$protocol_mask$partition0$ & (64))) || (map__71219.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__71219):map__71219);
var request = map__71219__$1;
var timeout = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71219__$1,cljs.core.cst$kw$timeout);
var callback_name = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71219__$1,cljs.core.cst$kw$callback_DASH_name);
var cancel = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71219__$1,cljs.core.cst$kw$cancel);
var keywordize_keys_QMARK_ = cljs.core.get.cljs$core$IFn$_invoke$arity$3(map__71219__$1,cljs.core.cst$kw$keywordize_DASH_keys_QMARK_,true);
var channel = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$0();
var jsonp__$1 = (new goog.net.Jsonp(cljs_http.util.build_url(request),callback_name));
jsonp__$1.setRequestTimeout(timeout);

var req_71235 = jsonp__$1.send(null,((function (channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_){
return (function cljs_http$core$jsonp_$_success_callback(data){
var response = new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$status,(200),cljs.core.cst$kw$success,true,cljs.core.cst$kw$body,cljs.core.js__GT_clj.cljs$core$IFn$_invoke$arity$variadic(data,cljs.core.array_seq([cljs.core.cst$kw$keywordize_DASH_keys,keywordize_keys_QMARK_], 0))], null);
cljs.core.async.put_BANG_.cljs$core$IFn$_invoke$arity$2(channel,response);

cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(cljs_http.core.pending_requests,cljs.core.dissoc,channel);

if(cljs.core.truth_(cancel)){
cljs.core.async.close_BANG_(cancel);
} else {
}

return cljs.core.async.close_BANG_(channel);
});})(channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_))
,((function (channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_){
return (function cljs_http$core$jsonp_$_error_callback(){
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$3(cljs_http.core.pending_requests,cljs.core.dissoc,channel);

if(cljs.core.truth_(cancel)){
cljs.core.async.close_BANG_(cancel);
} else {
}

return cljs.core.async.close_BANG_(channel);
});})(channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_))
);
cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$4(cljs_http.core.pending_requests,cljs.core.assoc,channel,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$jsonp,jsonp__$1,cljs.core.cst$kw$request,req_71235], null));

if(cljs.core.truth_(cancel)){
var c__42110__auto___71236 = cljs.core.async.chan.cljs$core$IFn$_invoke$arity$1((1));
cljs.core.async.impl.dispatch.run(((function (c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_){
return (function (){
var f__42111__auto__ = (function (){var switch__41984__auto__ = ((function (c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_){
return (function (state_71225){
var state_val_71226 = (state_71225[(1)]);
if((state_val_71226 === (1))){
var state_71225__$1 = state_71225;
return cljs.core.async.impl.ioc_helpers.take_BANG_(state_71225__$1,(2),cancel);
} else {
if((state_val_71226 === (2))){
var inst_71222 = (state_71225[(2)]);
var inst_71223 = jsonp__$1.cancel(req_71235);
var state_71225__$1 = (function (){var statearr_71227 = state_71225;
(statearr_71227[(7)] = inst_71222);

return statearr_71227;
})();
return cljs.core.async.impl.ioc_helpers.return_chan(state_71225__$1,inst_71223);
} else {
return null;
}
}
});})(c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_))
;
return ((function (switch__41984__auto__,c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_){
return (function() {
var cljs_http$core$jsonp_$_state_machine__41985__auto__ = null;
var cljs_http$core$jsonp_$_state_machine__41985__auto____0 = (function (){
var statearr_71231 = [null,null,null,null,null,null,null,null];
(statearr_71231[(0)] = cljs_http$core$jsonp_$_state_machine__41985__auto__);

(statearr_71231[(1)] = (1));

return statearr_71231;
});
var cljs_http$core$jsonp_$_state_machine__41985__auto____1 = (function (state_71225){
while(true){
var ret_value__41986__auto__ = (function (){try{while(true){
var result__41987__auto__ = switch__41984__auto__(state_71225);
if(cljs.core.keyword_identical_QMARK_(result__41987__auto__,cljs.core.cst$kw$recur)){
continue;
} else {
return result__41987__auto__;
}
break;
}
}catch (e71232){if((e71232 instanceof Object)){
var ex__41988__auto__ = e71232;
var statearr_71233_71237 = state_71225;
(statearr_71233_71237[(5)] = ex__41988__auto__);


cljs.core.async.impl.ioc_helpers.process_exception(state_71225);

return cljs.core.cst$kw$recur;
} else {
throw e71232;

}
}})();
if(cljs.core.keyword_identical_QMARK_(ret_value__41986__auto__,cljs.core.cst$kw$recur)){
var G__71238 = state_71225;
state_71225 = G__71238;
continue;
} else {
return ret_value__41986__auto__;
}
break;
}
});
cljs_http$core$jsonp_$_state_machine__41985__auto__ = function(state_71225){
switch(arguments.length){
case 0:
return cljs_http$core$jsonp_$_state_machine__41985__auto____0.call(this);
case 1:
return cljs_http$core$jsonp_$_state_machine__41985__auto____1.call(this,state_71225);
}
throw(new Error('Invalid arity: ' + arguments.length));
};
cljs_http$core$jsonp_$_state_machine__41985__auto__.cljs$core$IFn$_invoke$arity$0 = cljs_http$core$jsonp_$_state_machine__41985__auto____0;
cljs_http$core$jsonp_$_state_machine__41985__auto__.cljs$core$IFn$_invoke$arity$1 = cljs_http$core$jsonp_$_state_machine__41985__auto____1;
return cljs_http$core$jsonp_$_state_machine__41985__auto__;
})()
;})(switch__41984__auto__,c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_))
})();
var state__42112__auto__ = (function (){var statearr_71234 = (f__42111__auto__.cljs$core$IFn$_invoke$arity$0 ? f__42111__auto__.cljs$core$IFn$_invoke$arity$0() : f__42111__auto__.call(null));
(statearr_71234[cljs.core.async.impl.ioc_helpers.USER_START_IDX] = c__42110__auto___71236);

return statearr_71234;
})();
return cljs.core.async.impl.ioc_helpers.run_state_machine_wrapped(state__42112__auto__);
});})(c__42110__auto___71236,req_71235,channel,jsonp__$1,map__71219,map__71219__$1,request,timeout,callback_name,cancel,keywordize_keys_QMARK_))
);

} else {
}

return channel;
});
/**
 * Execute the HTTP request corresponding to the given Ring request
 *   map and return a core.async channel.
 */
cljs_http.core.request = (function cljs_http$core$request(p__71239){
var map__71242 = p__71239;
var map__71242__$1 = ((((!((map__71242 == null)))?((((map__71242.cljs$lang$protocol_mask$partition0$ & (64))) || (map__71242.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__71242):map__71242);
var request__$1 = map__71242__$1;
var request_method = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__71242__$1,cljs.core.cst$kw$request_DASH_method);
if(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(request_method,cljs.core.cst$kw$jsonp)){
return cljs_http.core.jsonp(request__$1);
} else {
return cljs_http.core.xhr(request__$1);
}
});
