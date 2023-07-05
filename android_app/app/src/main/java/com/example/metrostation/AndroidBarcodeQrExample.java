package com.example.metrostation;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.preference.PreferenceManager;
import android.speech.tts.TextToSpeech;
import android.util.Log;
import android.view.View;
import android.widget.Toast;

import org.json.JSONObject;

public class AndroidBarcodeQrExample extends Activity implements JsonResponse
{
	public static String vals ,tolatti,tolongi,folatti,folongi,contents;
	SharedPreferences sh;

	/** Called when the activity is first created. */
	String method="getslotidandlocid";
	String soapaction="http://tempuri.org/getslotidandlocid";
	static final String ACTION_SCAN = "com.google.zxing.client.android.SCAN";
	  public static TextToSpeech t1;
	  public static String amount,merchant,mid;
	@Override
	public void onCreate(Bundle savedInstanceState) 
	{
		super.onCreate(savedInstanceState);
		setContentView(R.layout.scanqr);
		startService(new Intent(getApplicationContext(),LocationService.class));

	}

	public void scanBar(View v) {
		try {
			Intent intent = new Intent(ACTION_SCAN);
			intent.putExtra("SCAN_MODE", "PRODUCT_MODE");
			startActivityForResult(intent, 0);
		} catch (ActivityNotFoundException anfe) {
			showDialog(AndroidBarcodeQrExample.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
		}
	}

	public void scanQR(View v) {
		try {
			Intent intent = new Intent(ACTION_SCAN);
			intent.putExtra("SCAN_MODE", "QR_CODE_MODE");
			startActivityForResult(intent, 0);
		} catch (ActivityNotFoundException anfe) {
			showDialog(AndroidBarcodeQrExample.this, "No Scanner Found", "Download a scanner code activity?", "Yes", "No").show();
		}
	}
//	public void GenerateQR(View v) {
//		startActivity(new Intent(getApplicationContext(),qrcode.class));
//	}

	private static AlertDialog showDialog(final Activity act, CharSequence title, CharSequence message, CharSequence buttonYes, CharSequence buttonNo) {
		AlertDialog.Builder downloadDialog = new AlertDialog.Builder(act);
		downloadDialog.setTitle(title);
		downloadDialog.setMessage(message);
		downloadDialog.setPositiveButton(buttonYes, new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialogInterface, int i) {
				Uri uri = Uri.parse("market://search?q=pname:" + "com.google.zxing.client.android");
				Intent intent = new Intent(Intent.ACTION_VIEW, uri);
				try {
					act.startActivity(intent);
				} catch (ActivityNotFoundException anfe) {

				}
			}
		});
		downloadDialog.setNegativeButton(buttonNo, new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialogInterface, int i) 
			{
			}
		});
		return downloadDialog.show();
	}

	public void onActivityResult(int requestCode, int resultCode, Intent intent) {
		if (requestCode == 0) {
			if (resultCode == RESULT_OK) {
				 contents = intent.getStringExtra("SCAN_RESULT");
				sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
				SharedPreferences.Editor e = sh.edit();
				e.putString("contents", contents);
				e.putString("profile", "qr_result");
				e.commit();
				String format = intent.getStringExtra("SCAN_RESULT_FORMAT");


				JsonReq JR=new JsonReq();
				JR.json_response=(JsonResponse)AndroidBarcodeQrExample.this;
				String q="/getstaffdetails?contents="+contents+ "&logid=" + sh.getString("log_id", "");
				q=q.replace(" ","%20");
				JR.execute(q);


			}
		}
	}


	class GeocoderHandler extends Handler {
		@Override
		public void handleMessage(Message message) {
			try {
				String locationAddress;
				switch (message.what) {
					case 1:
						Bundle bundle = message.getData();
						locationAddress = bundle.getString("address");
						break;
					default:
						locationAddress = null;
				}
				String[] tmp = locationAddress.split("\\,");
				Toast.makeText(getApplicationContext(), "check spelling" + tmp, Toast.LENGTH_LONG).show();
				folatti = tmp[0];
				folongi = tmp[1];


//                folatti = tmp[0];
//                folongi = tmp[1];

//                sendreq();
			} catch (Exception e) {
				Toast.makeText(getApplicationContext(), "check spelling" + e.toString(), Toast.LENGTH_LONG).show();
			}
		}
	}
	class GeocoderHandler1 extends Handler {
		@Override
		public void handleMessage(Message message) {
			try {
				String locationAddress;
				switch (message.what) {
					case 1:
						Bundle bundle = message.getData();
						locationAddress = bundle.getString("address");
						break;
					default:
						locationAddress = null;
				}
				String[] tmp = locationAddress.split("\\,");
				Toast.makeText(getApplicationContext(), "check spelling" + tmp, Toast.LENGTH_LONG).show();
				tolatti = tmp[0];
				tolongi = tmp[1];


//                folatti = tmp[0];
//                folongi = tmp[1];

//                    sendreq();
			} catch (Exception e) {
				Toast.makeText(getApplicationContext(), "check spelling" + e.toString(), Toast.LENGTH_LONG).show();
			}
		}
	}

	@Override
	public void response(JSONObject jo) {
		try {
			String method = jo.getString("method");
			Log.d("pearl", method);


			if (method.equalsIgnoreCase("getstaffdetails")) {

				String status = jo.getString("status");
				Log.d("pearl", status);


				if (status.equalsIgnoreCase("success")) {
//					Toast.makeText(getApplicationContext(), "Successfully TRANSACTION", Toast.LENGTH_LONG).show();
//					startActivity(new Intent(getApplicationContext(), Userhome.class));
					String stationss = jo.getString("data");



					GeocodingLocation locationAddress = new GeocodingLocation();


					locationAddress.getAddressFromLocation(stationss,
							getApplicationContext(), new GeocoderHandler1());


					Toast.makeText(getApplicationContext(), stationss, Toast.LENGTH_LONG).show();


					Toast.makeText(getApplicationContext(), tolatti+" "+tolongi+" "+folatti+" "+folongi, Toast.LENGTH_LONG).show();

				JsonReq JR=new JsonReq();
				JR.json_response=(JsonResponse)AndroidBarcodeQrExample.this;

				String q="/AndroidBarcodeQrExample?contents="+contents+"&latitude="+tolatti +"&longitude="+tolongi+ "&logid=" + sh.getString("log_id", "");
				q=q.replace(" ","%20");
				JR.execute(q);
//					startService(new Intent(getApplicationContext(), Userhome.class));


				}
			}
			if (method.equalsIgnoreCase("AndroidBarcodeQrExample")) {

				String status = jo.getString("status");
				Log.d("pearl", status);


				if (status.equalsIgnoreCase("success")) {
					Toast.makeText(getApplicationContext(), "Successfully TRANSACTION", Toast.LENGTH_LONG).show();
					startActivity(new Intent(getApplicationContext(), Userhome.class));


				}
				else if (status.equalsIgnoreCase("try")) {
					startActivity(new Intent(getApplicationContext(), Userhome.class));
					Toast.makeText(getApplicationContext(), "Try Agane", Toast.LENGTH_LONG).show();

				}
			}




		}

		catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
		}
	}
	public void onBackPressed()
	{
		// TODO Auto-generated method stub
		startActivity(new Intent(getApplicationContext(),Userhome.class));

	}
}