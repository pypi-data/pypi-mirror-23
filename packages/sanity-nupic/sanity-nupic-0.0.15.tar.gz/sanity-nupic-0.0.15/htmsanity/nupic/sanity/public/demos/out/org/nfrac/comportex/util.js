// Compiled by ClojureScript 1.9.229 {:static-fns true, :optimize-constants true}
goog.provide('org.nfrac.comportex.util');
goog.require('cljs.core');
goog.require('clojure.set');
goog.require('cljs.spec');
goog.require('cljs.spec.impl.gen');
goog.require('clojure.test.check.random');
/**
 * Like two-argument get, but throws an exception if the key is
 * not found.
 */
org.nfrac.comportex.util.getx = (function org$nfrac$comportex$util$getx(m,k){
var e = cljs.core.get.cljs$core$IFn$_invoke$arity$3(m,k,cljs.core.cst$kw$org$nfrac$comportex$util_SLASH_sentinel);
if(!(cljs.core._EQ_.cljs$core$IFn$_invoke$arity$2(e,cljs.core.cst$kw$org$nfrac$comportex$util_SLASH_sentinel))){
return e;
} else {
throw cljs.core.ex_info.cljs$core$IFn$_invoke$arity$2("Missing required key",new cljs.core.PersistentArrayMap(null, 2, [cljs.core.cst$kw$map,m,cljs.core.cst$kw$key,k], null));
}
});
/**
 * Like two-argument get-in, but throws an exception if the key is
 * not found.
 */
org.nfrac.comportex.util.getx_in = (function org$nfrac$comportex$util$getx_in(m,ks){
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3(org.nfrac.comportex.util.getx,m,ks);
});
org.nfrac.comportex.util.abs = (function org$nfrac$comportex$util$abs(x){
if((x < (0))){
return (- x);
} else {
return x;
}
});
org.nfrac.comportex.util.round = (function org$nfrac$comportex$util$round(var_args){
var args47494 = [];
var len__10461__auto___47498 = arguments.length;
var i__10462__auto___47499 = (0);
while(true){
if((i__10462__auto___47499 < len__10461__auto___47498)){
args47494.push((arguments[i__10462__auto___47499]));

var G__47500 = (i__10462__auto___47499 + (1));
i__10462__auto___47499 = G__47500;
continue;
} else {
}
break;
}

var G__47496 = args47494.length;
switch (G__47496) {
case 1:
return org.nfrac.comportex.util.round.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return org.nfrac.comportex.util.round.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args47494.length)].join('')));

}
});

org.nfrac.comportex.util.round.cljs$core$IFn$_invoke$arity$1 = (function (x){
var G__47497 = x;
return Math.round(G__47497);
});

org.nfrac.comportex.util.round.cljs$core$IFn$_invoke$arity$2 = (function (x,n){
var z = Math.pow(10.0,n);
return (org.nfrac.comportex.util.round.cljs$core$IFn$_invoke$arity$1((x * z)) / z);
});

org.nfrac.comportex.util.round.cljs$lang$maxFixedArity = 2;

org.nfrac.comportex.util.mean = (function org$nfrac$comportex$util$mean(xs){
return (cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,xs) / cljs.core.count(xs));
});
cljs.spec.def_impl(cljs.core.cst$kw$org$nfrac$comportex$util_SLASH_rng,cljs.core.list(cljs.core.cst$sym$cljs$core_SLASH__DASH__GT_,cljs.core.list(cljs.core.cst$sym$fn_STAR_,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.cst$sym$p1__47502_SHARP_], null),cljs.core.list(cljs.core.cst$sym$cljs$core_SLASH_satisfies_QMARK_,cljs.core.cst$sym$clojure$test$check$random_SLASH_IRandom,cljs.core.cst$sym$p1__47502_SHARP_)),cljs.core.list(cljs.core.cst$sym$cljs$spec_SLASH_with_DASH_gen,cljs.core.list(cljs.core.cst$sym$fn_STAR_,cljs.core.PersistentVector.EMPTY,cljs.core.list(cljs.core.cst$sym$cljs$spec$impl$gen_SLASH_fmap,cljs.core.cst$sym$clojure$test$check$random_SLASH_make_DASH_random,cljs.core.list(cljs.core.cst$sym$cljs$spec$impl$gen_SLASH_int))))),cljs.spec.with_gen((function (p1__47502_SHARP_){
if(!((p1__47502_SHARP_ == null))){
if((false) || (p1__47502_SHARP_.clojure$test$check$random$IRandom$)){
return true;
} else {
if((!p1__47502_SHARP_.cljs$lang$protocol_mask$partition$)){
return cljs.core.native_satisfies_QMARK_(clojure.test.check.random.IRandom,p1__47502_SHARP_);
} else {
return false;
}
}
} else {
return cljs.core.native_satisfies_QMARK_(clojure.test.check.random.IRandom,p1__47502_SHARP_);
}
}),(function (){
return cljs.spec.impl.gen.fmap.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([clojure.test.check.random.make_random,cljs.spec.impl.gen.int$()], 0));
})));
org.nfrac.comportex.util.rand = (function org$nfrac$comportex$util$rand(rng,lower,upper){
if((lower <= upper)){
} else {
throw (new Error("Assert failed: (<= lower upper)"));
}

return ((clojure.test.check.random.rand_double(rng) * (upper - lower)) + lower);
});
/**
 * Uniform integer between lower (inclusive) and upper (exclusive).
 */
org.nfrac.comportex.util.rand_int = (function org$nfrac$comportex$util$rand_int(var_args){
var args47504 = [];
var len__10461__auto___47509 = arguments.length;
var i__10462__auto___47510 = (0);
while(true){
if((i__10462__auto___47510 < len__10461__auto___47509)){
args47504.push((arguments[i__10462__auto___47510]));

var G__47511 = (i__10462__auto___47510 + (1));
i__10462__auto___47510 = G__47511;
continue;
} else {
}
break;
}

var G__47506 = args47504.length;
switch (G__47506) {
case 2:
return org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args47504.length)].join('')));

}
});

org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2 = (function (rng,upper){
return cljs.core.long$((function (){var G__47507 = (clojure.test.check.random.rand_double(rng) * upper);
return Math.floor(G__47507);
})());
});

org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$3 = (function (rng,lower,upper){
return cljs.core.long$((function (){var G__47508 = ((clojure.test.check.random.rand_double(rng) * (upper - lower)) + lower);
return Math.floor(G__47508);
})());
});

org.nfrac.comportex.util.rand_int.cljs$lang$maxFixedArity = 3;

org.nfrac.comportex.util.rand_nth = (function org$nfrac$comportex$util$rand_nth(rng,xs){
return cljs.core.nth.cljs$core$IFn$_invoke$arity$2(xs,org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2(rng,cljs.core.count(xs)));
});
/**
 * http://en.wikipedia.org/wiki/Fisher–Yates_shuffle#The_modern_algorithm
 */
org.nfrac.comportex.util.fisher_yates = (function org$nfrac$comportex$util$fisher_yates(rng,coll){
var as = cljs.core.object_array.cljs$core$IFn$_invoke$arity$1(coll);
var i = (cljs.core.count(as) - (1));
var r = rng;
while(true){
if(((1) <= i)){
var vec__47516 = clojure.test.check.random.split(r);
var r1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47516,(0),null);
var r2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47516,(1),null);
var j = org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2(r1,(i + (1)));
var t = (as[i]);
(as[i] = (as[j]));

(as[j] = t);

var G__47519 = (i - (1));
var G__47520 = r2;
i = G__47519;
r = G__47520;
continue;
} else {
return cljs.core.into.cljs$core$IFn$_invoke$arity$2(cljs.core.empty(coll),cljs.core.seq(as));
}
break;
}
});
org.nfrac.comportex.util.shuffle = (function org$nfrac$comportex$util$shuffle(rng,coll){
return org.nfrac.comportex.util.fisher_yates(rng,coll);
});
/**
 * Reservoir sample ct items from coll.
 */
org.nfrac.comportex.util.reservoir_sample = (function org$nfrac$comportex$util$reservoir_sample(rng,ct,coll){
var result = cljs.core.transient$(cljs.core.vec(cljs.core.take.cljs$core$IFn$_invoke$arity$2(ct,coll)));
var n = ct;
var coll__$1 = cljs.core.drop.cljs$core$IFn$_invoke$arity$2(ct,coll);
var r = rng;
while(true){
if(cljs.core.seq(coll__$1)){
var vec__47524 = clojure.test.check.random.split(r);
var r1 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47524,(0),null);
var r2 = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47524,(1),null);
var pos = org.nfrac.comportex.util.rand_int.cljs$core$IFn$_invoke$arity$2(r1,n);
var G__47527 = (((pos < ct))?cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(result,pos,cljs.core.first(coll__$1)):result);
var G__47528 = (n + (1));
var G__47529 = cljs.core.rest(coll__$1);
var G__47530 = r2;
result = G__47527;
n = G__47528;
coll__$1 = G__47529;
r = G__47530;
continue;
} else {
return cljs.core.persistent_BANG_(result);
}
break;
}
});
/**
 * Sample ct items with replacement (i.e. possibly with duplicates) from coll.
 */
org.nfrac.comportex.util.sample = (function org$nfrac$comportex$util$sample(rng,ct,coll){
if((ct > (0))){
return cljs.core.mapv.cljs$core$IFn$_invoke$arity$2((function (p1__47531_SHARP_){
return org.nfrac.comportex.util.rand_nth(p1__47531_SHARP_,coll);
}),clojure.test.check.random.split_n(rng,ct));
} else {
return null;
}
});
org.nfrac.comportex.util.quantile = (function org$nfrac$comportex$util$quantile(xs,p){
return cljs.core.nth.cljs$core$IFn$_invoke$arity$2(cljs.core.sort.cljs$core$IFn$_invoke$arity$1(xs),cljs.core.long$((p * (cljs.core.count(xs) - (1)))));
});
/**
 * Returns a function transforming uniform randoms in [0 1] to variates on a
 * Triangular distribution. http://en.wikipedia.org/wiki/Triangular_distribution
 * 
 * * a - lower bound
 * 
 * * b - upper bound
 * 
 * * c - peak of probability density (within bounds)
 */
org.nfrac.comportex.util.triangular = (function org$nfrac$comportex$util$triangular(a,b,c){
var Fc = ((c - a) / (b - a));
return ((function (Fc){
return (function (u){
if((u < Fc)){
return (a + (function (){var G__47534 = ((u * (b - a)) * (c - a));
return Math.sqrt(G__47534);
})());
} else {
return (b - (function (){var G__47535 = ((((1) - u) * (b - a)) * (b - c));
return Math.sqrt(G__47535);
})());
}
});
;})(Fc))
});
/**
 * Same as `(count (filter pred coll))`, but faster.
 */
org.nfrac.comportex.util.count_filter = (function org$nfrac$comportex$util$count_filter(pred,coll){
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (sum,x){
if(cljs.core.truth_((pred.cljs$core$IFn$_invoke$arity$1 ? pred.cljs$core$IFn$_invoke$arity$1(x) : pred.call(null,x)))){
return (sum + (1));
} else {
return sum;
}
}),(0),coll);
});
/**
 * Like the built-in group-by, but taking key-value pairs and building
 * maps instead of vectors for the groups. It is tuned for performance
 * with many values per key. `f` is a function taking 2 arguments, the
 * key and value.
 */
org.nfrac.comportex.util.group_by_maps = (function org$nfrac$comportex$util$group_by_maps(var_args){
var args47536 = [];
var len__10461__auto___47547 = arguments.length;
var i__10462__auto___47548 = (0);
while(true){
if((i__10462__auto___47548 < len__10461__auto___47547)){
args47536.push((arguments[i__10462__auto___47548]));

var G__47549 = (i__10462__auto___47548 + (1));
i__10462__auto___47548 = G__47549;
continue;
} else {
}
break;
}

var G__47538 = args47536.length;
switch (G__47538) {
case 2:
return org.nfrac.comportex.util.group_by_maps.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
case 3:
return org.nfrac.comportex.util.group_by_maps.cljs$core$IFn$_invoke$arity$3((arguments[(0)]),(arguments[(1)]),(arguments[(2)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args47536.length)].join('')));

}
});

org.nfrac.comportex.util.group_by_maps.cljs$core$IFn$_invoke$arity$2 = (function (f,kvs){
return org.nfrac.comportex.util.group_by_maps.cljs$core$IFn$_invoke$arity$3(f,kvs,cljs.core.PersistentArrayMap.EMPTY);
});

org.nfrac.comportex.util.group_by_maps.cljs$core$IFn$_invoke$arity$3 = (function (f,kvs,init_m){
return cljs.core.persistent_BANG_(cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (m,p__47539){
var vec__47540 = p__47539;
var g = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47540,(0),null);
var items = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47540,(1),null);
return cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(m,g,cljs.core.persistent_BANG_(items));
}),cljs.core.transient$(cljs.core.PersistentArrayMap.EMPTY),cljs.core.persistent_BANG_(cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (m,p__47543){
var vec__47544 = p__47543;
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47544,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47544,(1),null);
var g = (f.cljs$core$IFn$_invoke$arity$2 ? f.cljs$core$IFn$_invoke$arity$2(k,v) : f.call(null,k,v));
var items = cljs.core.get.cljs$core$IFn$_invoke$arity$3(m,g,cljs.core.transient$(init_m));
return cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(m,g,cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(items,k,v));
}),cljs.core.transient$(cljs.core.PersistentArrayMap.EMPTY),kvs))));
});

org.nfrac.comportex.util.group_by_maps.cljs$lang$maxFixedArity = 3;

/**
 * Transforms a transient map or vector `m` applying function `f` to
 *   the values under keys `ks`.
 */
org.nfrac.comportex.util.update_each_BANG_ = (function org$nfrac$comportex$util$update_each_BANG_(m,ks,f){
if(cljs.core.empty_QMARK_(ks)){
return m;
} else {
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (m__$1,k){
return cljs.core.assoc_BANG_.cljs$core$IFn$_invoke$arity$3(m__$1,k,(function (){var G__47552 = cljs.core.get.cljs$core$IFn$_invoke$arity$2(m__$1,k);
return (f.cljs$core$IFn$_invoke$arity$1 ? f.cljs$core$IFn$_invoke$arity$1(G__47552) : f.call(null,G__47552));
})());
}),m,ks);
}
});
/**
 * Transforms a map or vector `m` applying function `f` to the values
 *   under keys `ks`.
 */
org.nfrac.comportex.util.update_each = (function org$nfrac$comportex$util$update_each(m,ks,f){
if(cljs.core.empty_QMARK_(ks)){
return m;
} else {
return cljs.core.persistent_BANG_(org.nfrac.comportex.util.update_each_BANG_(cljs.core.transient$(m),ks,f));
}
});
org.nfrac.comportex.util.mapish_QMARK_ = (function org$nfrac$comportex$util$mapish_QMARK_(m){
return ((m == null)) || (cljs.core.map_QMARK_(m));
});
/**
 * Like merge-with, but merges maps recursively, applying the given fn
 *   only when there's a non-map at a particular level.
 */
org.nfrac.comportex.util.deep_merge_with = (function org$nfrac$comportex$util$deep_merge_with(var_args){
var args__10468__auto__ = [];
var len__10461__auto___47555 = arguments.length;
var i__10462__auto___47556 = (0);
while(true){
if((i__10462__auto___47556 < len__10461__auto___47555)){
args__10468__auto__.push((arguments[i__10462__auto___47556]));

var G__47557 = (i__10462__auto___47556 + (1));
i__10462__auto___47556 = G__47557;
continue;
} else {
}
break;
}

var argseq__10469__auto__ = ((((1) < args__10468__auto__.length))?(new cljs.core.IndexedSeq(args__10468__auto__.slice((1)),(0),null)):null);
return org.nfrac.comportex.util.deep_merge_with.cljs$core$IFn$_invoke$arity$variadic((arguments[(0)]),argseq__10469__auto__);
});

org.nfrac.comportex.util.deep_merge_with.cljs$core$IFn$_invoke$arity$variadic = (function (f,maps){
return cljs.core.apply.cljs$core$IFn$_invoke$arity$2((function() { 
var org$nfrac$comportex$util$m__delegate = function (maps__$1){
if(cljs.core.every_QMARK_(org.nfrac.comportex.util.mapish_QMARK_,maps__$1)){
return cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core.merge_with,org$nfrac$comportex$util$m,maps__$1);
} else {
return cljs.core.apply.cljs$core$IFn$_invoke$arity$2(f,maps__$1);
}
};
var org$nfrac$comportex$util$m = function (var_args){
var maps__$1 = null;
if (arguments.length > 0) {
var G__47558__i = 0, G__47558__a = new Array(arguments.length -  0);
while (G__47558__i < G__47558__a.length) {G__47558__a[G__47558__i] = arguments[G__47558__i + 0]; ++G__47558__i;}
  maps__$1 = new cljs.core.IndexedSeq(G__47558__a,0);
} 
return org$nfrac$comportex$util$m__delegate.call(this,maps__$1);};
org$nfrac$comportex$util$m.cljs$lang$maxFixedArity = 0;
org$nfrac$comportex$util$m.cljs$lang$applyTo = (function (arglist__47559){
var maps__$1 = cljs.core.seq(arglist__47559);
return org$nfrac$comportex$util$m__delegate(maps__$1);
});
org$nfrac$comportex$util$m.cljs$core$IFn$_invoke$arity$variadic = org$nfrac$comportex$util$m__delegate;
return org$nfrac$comportex$util$m;
})()
,maps);
});

org.nfrac.comportex.util.deep_merge_with.cljs$lang$maxFixedArity = (1);

org.nfrac.comportex.util.deep_merge_with.cljs$lang$applyTo = (function (seq47553){
var G__47554 = cljs.core.first(seq47553);
var seq47553__$1 = cljs.core.next(seq47553);
return org.nfrac.comportex.util.deep_merge_with.cljs$core$IFn$_invoke$arity$variadic(G__47554,seq47553__$1);
});

/**
 * Like merge, but merges maps recursively.
 */
org.nfrac.comportex.util.deep_merge = (function org$nfrac$comportex$util$deep_merge(var_args){
var args__10468__auto__ = [];
var len__10461__auto___47561 = arguments.length;
var i__10462__auto___47562 = (0);
while(true){
if((i__10462__auto___47562 < len__10461__auto___47561)){
args__10468__auto__.push((arguments[i__10462__auto___47562]));

var G__47563 = (i__10462__auto___47562 + (1));
i__10462__auto___47562 = G__47563;
continue;
} else {
}
break;
}

var argseq__10469__auto__ = ((((0) < args__10468__auto__.length))?(new cljs.core.IndexedSeq(args__10468__auto__.slice((0)),(0),null)):null);
return org.nfrac.comportex.util.deep_merge.cljs$core$IFn$_invoke$arity$variadic(argseq__10469__auto__);
});

org.nfrac.comportex.util.deep_merge.cljs$core$IFn$_invoke$arity$variadic = (function (maps){
if(cljs.core.every_QMARK_(org.nfrac.comportex.util.mapish_QMARK_,maps)){
return cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core.merge_with,org.nfrac.comportex.util.deep_merge,maps);
} else {
return cljs.core.last(maps);
}
});

org.nfrac.comportex.util.deep_merge.cljs$lang$maxFixedArity = (0);

org.nfrac.comportex.util.deep_merge.cljs$lang$applyTo = (function (seq47560){
return org.nfrac.comportex.util.deep_merge.cljs$core$IFn$_invoke$arity$variadic(cljs.core.seq(seq47560));
});

/**
 * Transforms a map `m` applying function `f` to each value.
 */
org.nfrac.comportex.util.remap = (function org$nfrac$comportex$util$remap(f,m){
return cljs.core.into.cljs$core$IFn$_invoke$arity$3((function (){var or__9278__auto__ = cljs.core.empty(m);
if(cljs.core.truth_(or__9278__auto__)){
return or__9278__auto__;
} else {
return cljs.core.PersistentArrayMap.EMPTY;
}
})(),cljs.core.map.cljs$core$IFn$_invoke$arity$1((function (p__47568){
var vec__47569 = p__47568;
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47569,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47569,(1),null);
return new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [k,(f.cljs$core$IFn$_invoke$arity$1 ? f.cljs$core$IFn$_invoke$arity$1(v) : f.call(null,v))], null);
})),m);
});
/**
 * Like `(reverse (take n (keys (sort-by val > m))))` but faster.
 */
org.nfrac.comportex.util.top_n_keys_by_value = (function org$nfrac$comportex$util$top_n_keys_by_value(n,m){
if((n <= (0))){
return cljs.core.PersistentVector.EMPTY;
} else {
if(cljs.core.empty_QMARK_(m)){
return cljs.core.PersistentVector.EMPTY;
} else {
if((n === (1))){
return new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.core.key(cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core.max_key,cljs.core.val,cljs.core.seq(m)))], null);
} else {
var ms = cljs.core.seq(m);
var am = cljs.core.sorted_map_by(((function (ms){
return (function (p1__47572_SHARP_,p2__47573_SHARP_){
return cljs.core.compare(new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(m.cljs$core$IFn$_invoke$arity$1 ? m.cljs$core$IFn$_invoke$arity$1(p1__47572_SHARP_) : m.call(null,p1__47572_SHARP_)),p1__47572_SHARP_], null),new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [(m.cljs$core$IFn$_invoke$arity$1 ? m.cljs$core$IFn$_invoke$arity$1(p2__47573_SHARP_) : m.call(null,p2__47573_SHARP_)),p2__47573_SHARP_], null));
});})(ms))
);
var curr_min = -1.0;
while(true){
if(cljs.core.empty_QMARK_(ms)){
return cljs.core.keys(am);
} else {
var vec__47577 = cljs.core.first(ms);
var k = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47577,(0),null);
var v = cljs.core.nth.cljs$core$IFn$_invoke$arity$3(vec__47577,(1),null);
if(cljs.core.empty_QMARK_(am)){
var G__47580 = cljs.core.next(ms);
var G__47581 = cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(am,k,v);
var G__47582 = v;
ms = G__47580;
am = G__47581;
curr_min = G__47582;
continue;
} else {
if((cljs.core.count(am) < n)){
var G__47583 = cljs.core.next(ms);
var G__47584 = cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(am,k,v);
var G__47585 = (function (){var x__9618__auto__ = curr_min;
var y__9619__auto__ = v;
return ((x__9618__auto__ < y__9619__auto__) ? x__9618__auto__ : y__9619__auto__);
})();
ms = G__47583;
am = G__47584;
curr_min = G__47585;
continue;
} else {
if((v > curr_min)){
var new_am = cljs.core.assoc.cljs$core$IFn$_invoke$arity$3(cljs.core.dissoc.cljs$core$IFn$_invoke$arity$2(am,cljs.core.first(cljs.core.keys(am))),k,v);
var G__47586 = cljs.core.next(ms);
var G__47587 = new_am;
var G__47588 = cljs.core.first(cljs.core.vals(new_am));
ms = G__47586;
am = G__47587;
curr_min = G__47588;
continue;
} else {
var G__47589 = cljs.core.next(ms);
var G__47590 = am;
var G__47591 = curr_min;
ms = G__47589;
am = G__47590;
curr_min = G__47591;
continue;

}
}
}
}
break;
}

}
}
}
});
/**
 * Returns a collection of
 *   `[(take w0 coll) (take w1 (drop w0 coll)) ...`
 *   and ending with a sequence containing the remainder.
 */
org.nfrac.comportex.util.splits_at = (function org$nfrac$comportex$util$splits_at(ws,coll){
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (subcolls,w){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(cljs.core.drop_last.cljs$core$IFn$_invoke$arity$1(subcolls),cljs.core.split_at(w,cljs.core.last(subcolls)));
}),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [coll], null),ws);
});
/**
 * Returns a collection of
 *   `[(take-while pred0 coll) (take-while pred1 (drop-while pred0 coll)) ...`
 *   and ending with a sequence containing the remainder.
 */
org.nfrac.comportex.util.splits_with = (function org$nfrac$comportex$util$splits_with(preds,coll){
return cljs.core.reduce.cljs$core$IFn$_invoke$arity$3((function (subcolls,pred){
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(cljs.core.drop_last.cljs$core$IFn$_invoke$arity$1(subcolls),cljs.core.split_with(pred,cljs.core.last(subcolls)));
}),new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [coll], null),preds);
});
/**
 * Using the provided widths and a coll of colls of indices, lazily adjust
 *   each index so that each coll of indices starts where the previous coll ended.
 *   Lazily concat all results.
 */
org.nfrac.comportex.util.align_indices = (function org$nfrac$comportex$util$align_indices(var_args){
var args47594 = [];
var len__10461__auto___47600 = arguments.length;
var i__10462__auto___47601 = (0);
while(true){
if((i__10462__auto___47601 < len__10461__auto___47600)){
args47594.push((arguments[i__10462__auto___47601]));

var G__47602 = (i__10462__auto___47601 + (1));
i__10462__auto___47601 = G__47602;
continue;
} else {
}
break;
}

var G__47596 = args47594.length;
switch (G__47596) {
case 1:
return org.nfrac.comportex.util.align_indices.cljs$core$IFn$_invoke$arity$1((arguments[(0)]));

break;
case 2:
return org.nfrac.comportex.util.align_indices.cljs$core$IFn$_invoke$arity$2((arguments[(0)]),(arguments[(1)]));

break;
default:
throw (new Error([cljs.core.str("Invalid arity: "),cljs.core.str(args47594.length)].join('')));

}
});

org.nfrac.comportex.util.align_indices.cljs$core$IFn$_invoke$arity$1 = (function (widths){
return cljs.core.cst$kw$not_DASH_implemented;
});

org.nfrac.comportex.util.align_indices.cljs$core$IFn$_invoke$arity$2 = (function (widths,collcoll){
var vec__47597 = collcoll;
var seq__47598 = cljs.core.seq(vec__47597);
var first__47599 = cljs.core.first(seq__47598);
var seq__47598__$1 = cljs.core.next(seq__47598);
var leftmost = first__47599;
var others = seq__47598__$1;
var offs = cljs.core.reductions.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,widths);
return cljs.core.concat.cljs$core$IFn$_invoke$arity$2(leftmost,cljs.core.mapcat.cljs$core$IFn$_invoke$arity$variadic(((function (vec__47597,seq__47598,first__47599,seq__47598__$1,leftmost,others,offs){
return (function (p1__47592_SHARP_,p2__47593_SHARP_){
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core._PLUS_,p1__47592_SHARP_),p2__47593_SHARP_);
});})(vec__47597,seq__47598,first__47599,seq__47598__$1,leftmost,others,offs))
,cljs.core.array_seq([offs,others], 0)));
});

org.nfrac.comportex.util.align_indices.cljs$lang$maxFixedArity = 2;

/**
 * Partition a sorted seq of indices into `(count widths)` seqs of unshifted
 *   indices. Determine boundaries via `widths`. `aligned-is` must be sorted.
 */
org.nfrac.comportex.util.unalign_indices = (function org$nfrac$comportex$util$unalign_indices(widths,aligned_is){
var offs = cljs.core.drop.cljs$core$IFn$_invoke$arity$2((1),cljs.core.reductions.cljs$core$IFn$_invoke$arity$3(cljs.core._PLUS_,(0),widths));
var vec__47608 = org.nfrac.comportex.util.splits_with(cljs.core.map.cljs$core$IFn$_invoke$arity$2(cljs.core.partial.cljs$core$IFn$_invoke$arity$2(cljs.core.partial,cljs.core._GT_),offs),aligned_is);
var seq__47609 = cljs.core.seq(vec__47608);
var first__47610 = cljs.core.first(seq__47609);
var seq__47609__$1 = cljs.core.next(seq__47609);
var leftmost = first__47610;
var others = seq__47609__$1;
var shifted = cljs.core.apply.cljs$core$IFn$_invoke$arity$3(cljs.core.vector,leftmost,cljs.core.map.cljs$core$IFn$_invoke$arity$3(((function (offs,vec__47608,seq__47609,first__47610,seq__47609__$1,leftmost,others){
return (function (section,offset){
return cljs.core.map.cljs$core$IFn$_invoke$arity$2(((function (offs,vec__47608,seq__47609,first__47610,seq__47609__$1,leftmost,others){
return (function (p1__47604_SHARP_){
return (p1__47604_SHARP_ - offset);
});})(offs,vec__47608,seq__47609,first__47610,seq__47609__$1,leftmost,others))
,section);
});})(offs,vec__47608,seq__47609,first__47610,seq__47609__$1,leftmost,others))
,others,offs));
if(cljs.core.empty_QMARK_(cljs.core.last(shifted))){
} else {
throw (new Error([cljs.core.str("Assert failed: "),cljs.core.str("No indices should be beyond the final offset."),cljs.core.str("\n"),cljs.core.str("(empty? (last shifted))")].join('')));
}

return cljs.core.drop_last.cljs$core$IFn$_invoke$arity$1(shifted);
});
org.nfrac.comportex.util.empty_queue = cljs.core.PersistentQueue.EMPTY;
/**
 * Returns a function that adds a metadata key `meta-key` to its
 * argument, being a #queue of the last `keep-n` values extracted
 * using `value-fn`.
 */
org.nfrac.comportex.util.keep_history_middleware = (function org$nfrac$comportex$util$keep_history_middleware(keep_n,value_fn,meta_key){
var hist = (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(org.nfrac.comportex.util.empty_queue) : cljs.core.atom.call(null,org.nfrac.comportex.util.empty_queue));
return ((function (hist){
return (function (x){
return cljs.core.vary_meta.cljs$core$IFn$_invoke$arity$4(x,cljs.core.assoc,meta_key,cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(hist,((function (hist){
return (function (h){
var h2 = cljs.core.conj.cljs$core$IFn$_invoke$arity$2(h,(value_fn.cljs$core$IFn$_invoke$arity$1 ? value_fn.cljs$core$IFn$_invoke$arity$1(x) : value_fn.call(null,x)));
if((cljs.core.count(h) >= keep_n)){
return cljs.core.pop(h2);
} else {
return h2;
}
});})(hist))
));
});
;})(hist))
});
/**
 * Returns a function that adds a metadata key `meta-key` to its
 * argument, being a map of the frequencies of values extracted
 * using `value-fn`.
 */
org.nfrac.comportex.util.frequencies_middleware = (function org$nfrac$comportex$util$frequencies_middleware(value_fn,meta_key){
var freqs = (function (){var G__47612 = cljs.core.PersistentArrayMap.EMPTY;
return (cljs.core.atom.cljs$core$IFn$_invoke$arity$1 ? cljs.core.atom.cljs$core$IFn$_invoke$arity$1(G__47612) : cljs.core.atom.call(null,G__47612));
})();
return ((function (freqs){
return (function (x){
return cljs.core.vary_meta.cljs$core$IFn$_invoke$arity$4(x,cljs.core.assoc,meta_key,cljs.core.swap_BANG_.cljs$core$IFn$_invoke$arity$2(freqs,((function (freqs){
return (function (m){
return cljs.core.update_in.cljs$core$IFn$_invoke$arity$3(m,new cljs.core.PersistentVector(null, 1, 5, cljs.core.PersistentVector.EMPTY_NODE, [(value_fn.cljs$core$IFn$_invoke$arity$1 ? value_fn.cljs$core$IFn$_invoke$arity$1(x) : value_fn.call(null,x))], null),cljs.core.fnil.cljs$core$IFn$_invoke$arity$2(cljs.core.inc,(0)));
});})(freqs))
));
});
;})(freqs))
});
org.nfrac.comportex.util.set_similarity = (function org$nfrac$comportex$util$set_similarity(sdr1,sdr2){
return (cljs.core.count(clojure.set.intersection.cljs$core$IFn$_invoke$arity$2(sdr1,sdr2)) / (function (){var x__9611__auto__ = (function (){var x__9611__auto__ = (1);
var y__9612__auto__ = cljs.core.count(sdr1);
return ((x__9611__auto__ > y__9612__auto__) ? x__9611__auto__ : y__9612__auto__);
})();
var y__9612__auto__ = cljs.core.count(sdr2);
return ((x__9611__auto__ > y__9612__auto__) ? x__9611__auto__ : y__9612__auto__);
})());
});
/**
 * Returns a generator of the return values of the function.
 *   The function must be given as a var and it must have arg specs.
 */
org.nfrac.comportex.util.fn__GT_generator = (function org$nfrac$comportex$util$fn__GT_generator(fn_var){
return cljs.spec.impl.gen.fmap.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([(function (p1__47613_SHARP_){
return cljs.core.apply.cljs$core$IFn$_invoke$arity$2(fn_var,p1__47613_SHARP_);
}),cljs.spec.gen.cljs$core$IFn$_invoke$arity$1(cljs.core.cst$kw$args.cljs$core$IFn$_invoke$arity$1(cljs.spec.get_spec(fn_var)))], 0));
});
org.nfrac.comportex.util.finite_QMARK_ = (function org$nfrac$comportex$util$finite_QMARK_(x){
if(typeof x === 'number'){
if(!(cljs.core.integer_QMARK_(x))){
return isFinite(x);
} else {
return true;
}
} else {
return null;
}
});
/**
 * Returns a spec like `number?` but which doesn't generate NaN or infinity.
 *   Specifically it accepts and generates integers or doubles. min/max optional.
 */
org.nfrac.comportex.util.spec_finite = (function org$nfrac$comportex$util$spec_finite(var_args){
var args__10468__auto__ = [];
var len__10461__auto___47618 = arguments.length;
var i__10462__auto___47619 = (0);
while(true){
if((i__10462__auto___47619 < len__10461__auto___47618)){
args__10468__auto__.push((arguments[i__10462__auto___47619]));

var G__47620 = (i__10462__auto___47619 + (1));
i__10462__auto___47619 = G__47620;
continue;
} else {
}
break;
}

var argseq__10469__auto__ = ((((0) < args__10468__auto__.length))?(new cljs.core.IndexedSeq(args__10468__auto__.slice((0)),(0),null)):null);
return org.nfrac.comportex.util.spec_finite.cljs$core$IFn$_invoke$arity$variadic(argseq__10469__auto__);
});

org.nfrac.comportex.util.spec_finite.cljs$core$IFn$_invoke$arity$variadic = (function (p__47615){
var map__47616 = p__47615;
var map__47616__$1 = ((((!((map__47616 == null)))?((((map__47616.cljs$lang$protocol_mask$partition0$ & (64))) || (map__47616.cljs$core$ISeq$))?true:false):false))?cljs.core.apply.cljs$core$IFn$_invoke$arity$2(cljs.core.hash_map,map__47616):map__47616);
var min = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__47616__$1,cljs.core.cst$kw$min);
var max = cljs.core.get.cljs$core$IFn$_invoke$arity$2(map__47616__$1,cljs.core.cst$kw$max);
return cljs.spec.with_gen(((function (map__47616,map__47616__$1,min,max){
return (function (x){
if(cljs.core.truth_(org.nfrac.comportex.util.finite_QMARK_(x))){
var and__9266__auto__ = (cljs.core.truth_(min)?(x >= min):true);
if(and__9266__auto__){
if(cljs.core.truth_(max)){
return (x <= max);
} else {
return true;
}
} else {
return and__9266__auto__;
}
} else {
return null;
}
});})(map__47616,map__47616__$1,min,max))
,(cljs.core.truth_((function (){var and__9266__auto__ = max;
if(cljs.core.truth_(and__9266__auto__)){
var and__9266__auto____$1 = min;
if(cljs.core.truth_(and__9266__auto____$1)){
return ((max - min) <= 1.0);
} else {
return and__9266__auto____$1;
}
} else {
return and__9266__auto__;
}
})())?((function (map__47616,map__47616__$1,min,max){
return (function (){
return cljs.spec.impl.gen.double_STAR_.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([new cljs.core.PersistentArrayMap(null, 3, [cljs.core.cst$kw$NaN_QMARK_,false,cljs.core.cst$kw$min,min,cljs.core.cst$kw$max,max], null)], 0));
});})(map__47616,map__47616__$1,min,max))
:((function (map__47616,map__47616__$1,min,max){
return (function (){
return cljs.spec.impl.gen.one_of.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([new cljs.core.PersistentVector(null, 2, 5, cljs.core.PersistentVector.EMPTY_NODE, [cljs.spec.impl.gen.large_integer.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([cljs.core.cst$kw$min,min,cljs.core.cst$kw$max,max], 0)),cljs.spec.impl.gen.double_STAR_.cljs$core$IFn$_invoke$arity$variadic(cljs.core.array_seq([new cljs.core.PersistentArrayMap(null, 4, [cljs.core.cst$kw$NaN_QMARK_,false,cljs.core.cst$kw$infinite_QMARK_,false,cljs.core.cst$kw$min,min,cljs.core.cst$kw$max,max], null)], 0))], null)], 0));
});})(map__47616,map__47616__$1,min,max))
));
});

org.nfrac.comportex.util.spec_finite.cljs$lang$maxFixedArity = (0);

org.nfrac.comportex.util.spec_finite.cljs$lang$applyTo = (function (seq47614){
return org.nfrac.comportex.util.spec_finite.cljs$core$IFn$_invoke$arity$variadic(cljs.core.seq(seq47614));
});

