/* global googletag */

const SLOT_PREFIX = '/5805113/';

(function() {
  var gads = document.createElement('script');
  gads.async = true;
  gads.type = 'text/javascript';
  var useSSL = document.location.protocol === 'https:';
  gads.src =
    (useSSL ? 'https:' : 'http:') + '//www.googletagservices.com/tag/js/gpt.js';
  var node = document.getElementsByTagName('script')[0];
  node.parentNode.insertBefore(gads, node);
})();

googletag.cmd.push(function() {
  googletag.pubads().setTargeting('tribpedia', 'public-schools');

  var bannerMapping = googletag
    .sizeMapping()
    .addSize([768, 1], [728, 90])
    .addSize([0, 0], [300, 250])
    .build();

  googletag
    .defineSlot(
      `${SLOT_PREFIX}TexasTribune_Site_Roofline1_ATF_Leaderboard_728x90`,
      [728, 90],
      'ad-banner-leader'
    )
    .defineSizeMapping(bannerMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(`${SLOT_PREFIX}basic`, [728, 90], 'ad-banner-middle-1')
    .defineSizeMapping(bannerMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(`${SLOT_PREFIX}basic`, [728, 90], 'ad-banner-middle-2')
    .defineSizeMapping(bannerMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(`${SLOT_PREFIX}basic`, [300, 250], 'ad-sidebar')
    .addService(googletag.pubads());

  googletag
    .defineSlot(
      `${SLOT_PREFIX}TexasTribune_Content_StoryLanding_BTF_Footer_Leaderboard_728x90`,
      [728, 90],
      'ad-banner-footer'
    )
    .defineSizeMapping(bannerMapping)
    .addService(googletag.pubads());

  googletag.pubads().enableSingleRequest();
  googletag.enableServices();
});

googletag.cmd.push(function() {
  googletag.display('ad-banner-leader');
  googletag.display('ad-banner-middle-1');
  googletag.display('ad-sidebar');
  googletag.display('ad-banner-middle-2');
  googletag.display('ad-banner-footer');
});
