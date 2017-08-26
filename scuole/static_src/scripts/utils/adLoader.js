/* global googletag */

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

  var metricsMapping = googletag
    .sizeMapping()
    .addSize([510, 1], [468, 60])
    .addSize([0, 0], [300, 250])
    .build();

  googletag
    .defineSlot(
      '/5805113/TexasTribune_Data_DataPage_ATF_Header_Leaderboard_728x90',
      [728, 90],
      'ad-banner-leader'
    )
    .defineSizeMapping(bannerMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(
      '/5805113/TexasTribune_Data_DataPage_ATF_RightRail1_MediumRectangle_300x250',
      [300, 250],
      'ad-sidebar'
    )
    .addService(googletag.pubads());

  googletag
    .defineSlot(
      '/5805113/TexasTribune_Content_StoryPage_InsideStory_468x60',
      [468, 60],
      'ad-metrics-1'
    )
    .defineSizeMapping(metricsMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(
      '/5805113/TexasTribune_Content_StoryPage_InsideStory2_468x60',
      [468, 60],
      'ad-metrics-2'
    )
    .defineSizeMapping(metricsMapping)
    .addService(googletag.pubads());

  googletag
    .defineSlot(
      '/5805113/TexasTribune_Data_DataPage_BTF_Footer_Leaderboard_728x90',
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
  googletag.display('ad-sidebar');
  googletag.display('ad-metrics-1');
  googletag.display('ad-metrics-2');
  googletag.display('ad-banner-footer');
});
