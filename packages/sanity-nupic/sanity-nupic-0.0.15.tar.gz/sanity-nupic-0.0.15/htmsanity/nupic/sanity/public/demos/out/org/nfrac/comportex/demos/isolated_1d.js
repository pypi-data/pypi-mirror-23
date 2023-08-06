// Compiled by ClojureScript 1.9.229 {:static-fns true, :optimize-constants true}
goog.provide('org.nfrac.comportex.demos.isolated_1d');
goog.require('cljs.core');
goog.require('org.nfrac.comportex.core');
goog.require('clojure.test.check.random');
goog.require('org.nfrac.comportex.util');
goog.require('org.nfrac.comportex.encoders');
goog.require('org.nfrac.comportex.layer');
org.nfrac.comportex.demos.isolated_1d.bit_width = (300);
org.nfrac.comportex.demos.isolated_1d.n_on_bits = (20);
org.nfrac.comportex.demos.isolated_1d.numb_max = (15);
org.nfrac.comportex.demos.isolated_1d.numb_domain = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),org.nfrac.comportex.demos.isolated_1d.numb_max], null);
org.nfrac.comportex.demos.isolated_1d.radius = org.nfrac.comportex.demos.isolated_1d.n_on_bits;
org.nfrac.comportex.demos.isolated_1d.resolution = (((2) * org.nfrac.comportex.demos.isolated_1d.radius) * 0.8);
org.nfrac.comportex.demos.isolated_1d.params = new cljs.core.PersistentArrayMap(null, 5, [cljs.core.cst$kw$column_DASH_dimensions,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(1000)], null),cljs.core.cst$kw$ff_DASH_init_DASH_frac,0.2,cljs.core.cst$kw$ff_DASH_potential_DASH_radius,1.0,cljs.core.cst$kw$proximal,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$perm_DASH_inc,0.1,cljs.core.cst$kw$perm_DASH_dec,0.01], null),cljs.core.cst$kw$duty_DASH_cycle_DASH_period,(100000)], null);
org.nfrac.comportex.demos.isolated_1d.higher_level_params = org.nfrac.comportex.util.deep_merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([org.nfrac.comportex.demos.isolated_1d.params,new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$column_DASH_dimensions,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(400)], null),cljs.core.cst$kw$proximal,new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$max_DASH_segments,(5)], null)], null)], 0));
org.nfrac.comportex.demos.isolated_1d.patterns = new cljs.core.PersistentArrayMap(null, 6, [cljs.core.cst$kw$run_DASH_0_DASH_5,new cljs.core.PersistentVector(null, 6, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),(1),(2),(3),(4),(5)], null),cljs.core.cst$kw$rev_DASH_5_DASH_1,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(5),(4),(3),(2),(1)], null),cljs.core.cst$kw$run_DASH_6_DASH_10,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(6),(7),(8),(9),(10)], null),cljs.core.cst$kw$jump_DASH_6_DASH_12,new cljs.core.PersistentVector(null, 5, 5, cljs.core.PersistentVector.EMPTY_NODE, [(6),(7),(8),(11),(12)], null),cljs.core.cst$kw$twos,new cljs.core.PersistentVector(null, 8, 5, cljs.core.PersistentVector.EMPTY_NODE, [(0),(2),(4),(6),(8),(10),(12),(14)], null),cljs.core.cst$kw$saw_DASH_10_DASH_15,new cljs.core.PersistentVector(null, 8, 5, cljs.core.PersistentVector.EMPTY_NODE, [(10),(12),(11),(13),(12),(14),(13),(15)], null)], null);
org.nfrac.comportex.demos.isolated_1d.pattern_order = cljs.core.keys(org.nfrac.comportex.demos.isolated_1d.patterns);
org.nfrac.comportex.demos.isolated_1d.gap_length = (5);
org.nfrac.comportex.demos.isolated_1d.initial_world = (function org$nfrac$comportex$demos$isolated_1d$initial_world(){
var id = cljs.core.first(org.nfrac.comportex.demos.isolated_1d.pattern_order);
var values = (org.nfrac.comportex.demos.isolated_1d.patterns.cljs$core$IFn$_invoke$arity$1 ? org.nfrac.comportex.demos.isolated_1d.patterns.cljs$core$IFn$_invoke$arity$1(id) : org.nfrac.comportex.demos.isolated_1d.patterns.call(null,id));
return cljs.core.vary_meta.cljs$core$IFn$_invoke$arity$4(new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$id,id,cljs.core.cst$kw$values,values,cljs.core.cst$kw$index,(0)], null),cljs.core.assoc,cljs.core.cst$kw$org$nfrac$comportex$demos$isolated_DASH_1d_SLASH_rng,clojure.test.check.random.make_random.cljs$core$IFn$_invoke$arity$1((42)));
});
org.nfrac.comportex.demos.isolated_1d.world_transform = (function org$nfrac$comportex$demos$isolated_1d$world_transform(p__81921){
var map__81927 = p__81921;
var map__81927__$1 = ((((!((map__81927 == null)))?((((map__81927.cljs$lang$protocol_mask$partition0$ & (64))) || (map__81927.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__81927):map__81927);
var input = map__81927__$1;
var id = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__81927__$1,cljs.core.cst$kw$id);
var values = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__81927__$1,cljs.core.cst$kw$values);
var index = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__81927__$1,cljs.core.cst$kw$index);
if((index < (cljs.core.count(values) - (1)))){
return cljs.core.update_in.cljs$core$IFn$_invoke$arity$3(input,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$index], null),cljs.core.inc);
} else {
if(cljs.core.truth_(id)){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$variadic(input,cljs.core.cst$kw$id,null,cljs.core.array_seq([cljs.core.cst$kw$values,cljs.core.repeat.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.demos.isolated_1d.gap_length,null),cljs.core.cst$kw$index,(0)], 0));
} else {
var vec__81929 = clojure.test.check.random.split(cljs.core.cst$kw$org$nfrac$comportex$demos$isolated_DASH_1d_SLASH_rng.cljs$core$IFn$_invoke$arity$1(cljs.core.meta(input)));
var rng = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__81929,(0),null);
var rng_STAR_ = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__81929,(1),null);
var id__$1 = org.nfrac.comportex.util.rand_nth(rng_STAR_,org.nfrac.comportex.demos.isolated_1d.pattern_order);
return cljs.core.vary_meta.cljs$core$IFn$_invoke$arity$4(new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$id,id__$1,cljs.core.cst$kw$values,(org.nfrac.comportex.demos.isolated_1d.patterns.cljs$core$IFn$_invoke$arity$1 ? org.nfrac.comportex.demos.isolated_1d.patterns.cljs$core$IFn$_invoke$arity$1(id__$1) : org.nfrac.comportex.demos.isolated_1d.patterns.call(null,id__$1)),cljs.core.cst$kw$index,(0)], null),cljs.core.assoc,cljs.core.cst$kw$org$nfrac$comportex$demos$isolated_DASH_1d_SLASH_rng,rng);
}
}
});
org.nfrac.comportex.demos.isolated_1d.attach_current_value = (function org$nfrac$comportex$demos$isolated_1d$attach_current_value(m){
return cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(m,cljs.core.cst$kw$value,cljs.core.get.cljs$core$IFn$_invoke$arity$2(cljs.core.cst$kw$values.cljs$core$IFn$_invoke$arity$1(m),cljs.core.cst$kw$index.cljs$core$IFn$_invoke$arity$1(m)));
});
/**
 * Returns an infinite lazy seq of sensory input values.
 */
org.nfrac.comportex.demos.isolated_1d.input_seq = (function org$nfrac$comportex$demos$isolated_1d$input_seq(){
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(org.nfrac.comportex.demos.isolated_1d.attach_current_value,cljs.core.iterate(org.nfrac.comportex.demos.isolated_1d.world_transform,org.nfrac.comportex.demos.isolated_1d.initial_world()));
});
org.nfrac.comportex.demos.isolated_1d.block_sensor = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$kw$value,org.nfrac.comportex.encoders.linear_encoder.cljs$core$IFn$_invoke$arity$3(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.demos.isolated_1d.bit_width], null),org.nfrac.comportex.demos.isolated_1d.n_on_bits,org.nfrac.comportex.demos.isolated_1d.numb_domain)], null);
org.nfrac.comportex.demos.isolated_1d.coord_sensor = new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.encoders.vec_selector.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([cljs.core.cst$kw$value], 0)),org.nfrac.comportex.encoders.coordinate_encoder(new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.demos.isolated_1d.bit_width], null),org.nfrac.comportex.demos.isolated_1d.n_on_bits,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.demos.isolated_1d.resolution], null),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [org.nfrac.comportex.demos.isolated_1d.radius], null))], null);
org.nfrac.comportex.demos.isolated_1d.build = (function org$nfrac$comportex$demos$isolated_1d$build(var_args){
var args81932 = [];
var len__10461__auto___81935 = arguments.length;
var i__10462__auto___81936 = (0);
while(true){
if((i__10462__auto___81936 < len__10461__auto___81935)){
args81932.push((arguments[i__10462__auto___81936]));

var G__81937 = (i__10462__auto___81936 + (1));
i__10462__auto___81936 = G__81937;
continue;
} else {
}
break;
}

var G__81934 = args81932.length;
switch (G__81934) {
case 0:
return org.nfrac.comportex.demos.isolated_1d.build.cljs$core$IFn$_invoke$arity$0();

break;
case 1:
return org.nfrac.comportex.demos.isolated_1d.build.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args81932.length)].join('')));

}
});

org.nfrac.comportex.demos.isolated_1d.build.cljs$core$IFn$_invoke$arity$0 = (function (){
return org.nfrac.comportex.demos.isolated_1d.build.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.demos.isolated_1d.params);
});

org.nfrac.comportex.demos.isolated_1d.build.cljs$core$IFn$_invoke$arity$1 = (function (params){
return org.nfrac.comportex.core.network.cljs$core$IFn$_invoke$arity$2(new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$layer_DASH_a,org.nfrac.comportex.layer.layer_of_cells(params)], null),new cljs.core.PersistentArrayMap(null, 1, [cljs.core.cst$kw$input,org.nfrac.comportex.demos.isolated_1d.block_sensor], null));
});

org.nfrac.comportex.demos.isolated_1d.build.cljs$lang$maxFixedArity = 1;

