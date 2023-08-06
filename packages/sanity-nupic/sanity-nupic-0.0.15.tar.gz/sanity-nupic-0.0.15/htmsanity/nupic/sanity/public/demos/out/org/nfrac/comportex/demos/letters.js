// Compiled by ClojureScript 1.9.229 {:static-fns true, :optimize-constants true}
goog.provide('org.nfrac.comportex.demos.letters');
goog.require('cljs.core');
goog.require('org.nfrac.comportex.core');
goog.require('org.nfrac.comportex.util');
goog.require('org.nfrac.comportex.encoders');
goog.require('org.nfrac.comportex.layer');
goog.require('clojure.string');
org.nfrac.comportex.demos.letters.bit_width = (500);
org.nfrac.comportex.demos.letters.n_on_bits = (25);
org.nfrac.comportex.demos.letters.params = new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$column_DASH_dimensions,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(1000)], null),cljs.core.cst$kw$depth,(8),cljs.core.cst$kw$distal,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$perm_DASH_init,0.21], null),cljs.core.cst$kw$distal_DASH_vs_DASH_proximal_DASH_weight,0.2], null);
org.nfrac.comportex.demos.letters.higher_level_params = org.nfrac.comportex.util.deep_merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([org.nfrac.comportex.demos.letters.params,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$column_DASH_dimensions,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(800)], null),cljs.core.cst$kw$proximal,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$max_DASH_segments,(5)], null)], null)], 0));
org.nfrac.comportex.demos.letters.clean_text = (function org$nfrac$comportex$demos$letters$clean_text(text){
return clojure.string.replace(clojure.string.lower_case(text),/\s+/," ");
});
org.nfrac.comportex.demos.letters.random_sensor = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$value,org.nfrac.comportex.encoders.unique_encoder(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.demos.letters.bit_width], null),org.nfrac.comportex.demos.letters.n_on_bits)], null);
org.nfrac.comportex.demos.letters.build = (function org$nfrac$comportex$demos$letters$build(var_args){
var args83236 = [];
var len__10461__auto___83239 = arguments.length;
var i__10462__auto___83240 = (0);
while(true){
if((i__10462__auto___83240 < len__10461__auto___83239)){
args83236.push((arguments[i__10462__auto___83240]));

var G__83241 = (i__10462__auto___83240 + (1));
i__10462__auto___83240 = G__83241;
continue;
} else {
}
break;
}

var G__83238 = args83236.length;
switch (G__83238) {
case 0:
return org.nfrac.comportex.demos.letters.build.cljs$core$IFn$_invoke$arity$0();

break;
case 1:
return org.nfrac.comportex.demos.letters.build.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args83236.length)].join('')));

}
});

org.nfrac.comportex.demos.letters.build.cljs$core$IFn$_invoke$arity$0 = (function (){
return org.nfrac.comportex.demos.letters.build.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.demos.letters.params);
});

org.nfrac.comportex.demos.letters.build.cljs$core$IFn$_invoke$arity$1 = (function (params){
return org.nfrac.comportex.core.network.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$layer_DASH_a,org.nfrac.comportex.layer.layer_of_cells(params)], null),new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$input,org.nfrac.comportex.demos.letters.random_sensor], null));
});

org.nfrac.comportex.demos.letters.build.cljs$lang$maxFixedArity = 1;

