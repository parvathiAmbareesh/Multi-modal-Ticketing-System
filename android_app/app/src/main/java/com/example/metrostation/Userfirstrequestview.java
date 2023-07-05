package com.example.metrostation;

import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

import org.json.JSONArray;
import org.json.JSONObject;

public class Userfirstrequestview extends AppCompatActivity implements JsonResponse, AdapterView.OnItemClickListener {



    ListView l1;

    public static String amtss,rid,amts;

    SharedPreferences sh;

    String[] request_id,date,amount,fplaces,tplaces,value,total;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_userfirstrequestview);


        sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        l1=(ListView)findViewById(R.id.lv);

        l1.setOnItemClickListener(this);


        JsonReq JR = new JsonReq();
        JR.json_response = (JsonResponse) Userfirstrequestview.this;
        String q = "/Userfirstrequestview?lid="+sh.getString("log_id", "");
        q = q.replace(" ", "%20");
        JR.execute(q);





    }

    @Override
    public void response(JSONObject jo) {
        try {

            String method=jo.getString("method");
            if(method.equalsIgnoreCase("AddRequest")) {

                String status = jo.getString("status");
                Log.d("pearl", status);


                if (status.equalsIgnoreCase("success")) {
                    Toast.makeText(getApplicationContext(), "ADDED SUCCESSFULLY", Toast.LENGTH_LONG).show();
                    String rid=jo.getString("rid");

                    SharedPreferences.Editor e = sh.edit();
                    e.putString("rid", rid);
                    e.commit();

                    startActivity(new Intent(getApplicationContext(), Userviewrequest.class));

                } else {

                    Toast.makeText(getApplicationContext(), " failed.TRY AGAIN!!", Toast.LENGTH_LONG).show();
                }
            }
            else if(method.equalsIgnoreCase("Userfirstrequestview"))
            {
                String status=jo.getString("status");
                Log.d("pearl",status);


                if(status.equalsIgnoreCase("success")){
                    JSONArray ja1=(JSONArray)jo.getJSONArray("data");

                    request_id=new String[ja1.length()];
                    date=new String[ja1.length()];
                    amount=new String[ja1.length()];
                    fplaces=new String[ja1.length()];
                    tplaces=new String[ja1.length()];
                    value=new String[ja1.length()];
                    total=new String[ja1.length()];


                    for(int i = 0;i<ja1.length();i++)
                    {
                        request_id[i]=ja1.getJSONObject(i).getString("request_id");
                        date[i]=ja1.getJSONObject(i).getString("date");
                        amount[i]=ja1.getJSONObject(i).getString("amount");
                        total[i]=ja1.getJSONObject(i).getString("totals");
                        fplaces[i]=ja1.getJSONObject(i).getString("fplace");
                        tplaces[i]=ja1.getJSONObject(i).getString("tplace");


                        value[i]="Date : "+date[i]+"\nAmount : "+amount[i]+"\nFrom Place : "+fplaces[i]+"\nto Places : "+tplaces[i];


                    }
                    ArrayAdapter<String> ar=new ArrayAdapter<String>(getApplicationContext(),R.layout.custtext,value);
                    l1.setAdapter(ar);
                }
            }



        }

        catch (Exception e) {
            // TODO: handle exception
            e.printStackTrace();
            Toast.makeText(getApplicationContext(), e.toString(), Toast.LENGTH_LONG).show();
        }
    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {

        rid=request_id[i];
        amts=amount[i];

        amtss=total[i];


        final CharSequence[] items = {"start trip","Cancel"};

        AlertDialog.Builder builder = new AlertDialog.Builder(Userfirstrequestview.this);
        // builder.setTitle("Add Photo!");
        builder.setItems(items, new DialogInterface.OnClickListener() {
            @Override
            public void onClick(DialogInterface dialog, int item) {

                if (items[item].equals("start trip")) {

                startActivity(new Intent(getApplicationContext(),Addplace.class));

                }

                else if (items[item].equals("Cancel")) {
                    dialog.dismiss();
                }

            }

        });
        builder.show();
    }
    }
