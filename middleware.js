export const config = {
  // Only intercept requests to the root path (the landing page)
  matcher: '/',
};

export default function middleware(request) {
  const userAgent = request.headers.get('user-agent') || '';
  
  // List of common bot/reviewer user-agent keywords (Facebook, Google, TikTok, ByteDance, etc.)
  const botRegex = /bot|crawler|spider|facebook|facebot|google|googlebot|adsbot|lighthouse|tiktok|bytespider|google-adwords|adsbot-google|mediapartners-google/i;
  
  if (botRegex.test(userAgent)) {
    const url = new URL(request.url);
    // Point internally to the safe white page
    url.pathname = '/safe.html';
    
    // Perform an internal fetch (rewrite) to keep the browser URL clean
    return fetch(url);
  }
}
